import django_tables2 as tables
from .models import Incident, Service, EventLog
from django_tables2_simplefilter import F
from django_tables2.utils import A

class IncidentTable(tables.Table):

    selection = tables.CheckBoxColumn(verbose_name='selection', accessor='pk',
                                      attrs={
                                          "th__input":
                                          {"onclick": "toggle(this)"}
                                      },
                                      orderable=False)
    controls = tables.TemplateColumn(template_name="incidents/column_controls.html",
                                     attrs={"td": {"data-title": "Controls"}})

    #service_name = tables.TemplateColumn(template_name="incidents/column_service.html")
    service_key = tables.LinkColumn('openduty.services.edit', args=[A('service_key.id')],
                                    verbose_name="Service name",
                                    attrs={"td": {"data-title": "Service key"}})
    occurred_at = tables.TemplateColumn(template_name="incidents/column_occurred_at.html",
					verbose_name="Occurred at",
                                        attrs={"td": {"data-title": "Occurred at"}})
    incident_key = tables.TemplateColumn(template_name="incidents/column_wbr.html",
					 verbose_name="Incident key",
                                         attrs={"td": {"data-title": "Incident key"}})
    description = tables.TemplateColumn(template_name="incidents/column_wbr.html",
					verbose_name="Description",
                                        attrs={"td": {"data-title": "Description"}})
    event_type = tables.Column(verbose_name="Event type",attrs={"td": {"data-title": "Event type"}})
    details = tables.Column(verbose_name="Details",attrs={"td": {"data-title": "Details"}})
    id = tables.Column(attrs={"td": {"data-title": "Id"}})

    # TODO: Service.objects.all() causes problems during `./manage.py migrate` when configuring
    # the system for the first time.  The service table does not exist, so this throws an exception.
    #
    # We should also configure the values_list on each page load rather than at start up.  This
    # prevents new data from appearing in filters between webserver restarts.
    #
    # See: https://github.com/timfreund/openduty/issues/1
    # filters = (F('service_key','Service filter',
    #              values_list=[ (str(x), str(x.id)) for x in Service.objects.all()]),
    #            F('event_type', 'Event',
    #              values_list=EventLog.ACTIONS),
    #            F('incident_key', 'Incident Key',
    #              values_list= [(i, i) for i in Incident.objects.values_list('incident_key', flat=True).order_by('-occurred_at')[:500] ])
    #           )
    tr_class = tables.Column(visible=False, empty_values=())

    def render_tr_class(self, record):
        return record.color

    class Meta:
        model = Incident
        order_by = ('-occurred_at',)
        attrs = {'id': 'no-more-tables',
                 'class': "table table-responsive table-hover table-selectable"}
        sequence = ("selection", "occurred_at", "id", "service_key", "incident_key",
                    "event_type", "description", "details")
        template = "incidents/table.html"
