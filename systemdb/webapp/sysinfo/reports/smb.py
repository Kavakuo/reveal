from flask import render_template, Response, url_for, request
from flask_login import login_required
from sqlalchemy import and_

from systemdb.webapp.sysinfo import sysinfo_bp
from systemdb.core.export.excel.hosts import generate_hosts_excel
from systemdb.core.export.excel.hosts import generate_hosts_excel_brief
from systemdb.core.models.sysinfo import Host
from systemdb.core.reports import ReportInfo
from systemdb.webapp.sysinfo.forms.report.SMBv1Report import SMBv1ReportForm

####################################################################
# Hosts with enabled SMBv1
####################################################################
@sysinfo_bp.route('/report/smbv1', methods=['GET', 'POST'])
@login_required
def hosts_report_smbv1():
    form = SMBv1ReportForm()

    filter = []
    filter.append(Host.SMBv1Enabled == True)

    if request.method == 'POST':

        if form.validate_on_submit():
            systemgroup = form.SystemGroup.data
            location = form.Location.data

            invertSystemgroup = form.InvertSystemGroup.data
            invertLocation = form.InvertLocation.data

            if len(systemgroup) > 0:
                if not invertSystemgroup:
                    filter.append(Host.SystemGroup.ilike("%" + systemgroup + "%"))
                else:
                    filter.append(Host.SystemGroup.notilike("%" + systemgroup + "%"))
            if len(location) > 0:
                if not invertLocation:
                    filter.append(Host.Location.ilike("%" + location + "%"))
                else:
                    filter.append(Host.Location.notilike("%" + location + "%"))

            hosts = Host.query.filter(and_(*filter)).all()

            if 'brief' in request.form:
                output = generate_hosts_excel_brief(hosts)
                return Response(output, mimetype="text/xlsx",
                                headers={"Content-disposition": "attachment; filename=hosts-with-smbv1-brief.xlsx",
                                         "Content-type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"})
            if 'full' in request.form:
                output = generate_hosts_excel(hosts)
                return Response(output, mimetype="text/xlsx",
                                headers={"Content-disposition": "attachment; filename=hosts-with-smbv1-full.xlsx",
                                         "Content-type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"})

    else:
        hosts = Host.query.filter(and_(*filter)).all()
    return render_template('sysinfo/reports/host_report_list.html', hosts=hosts, form=form)



class ReportSMBv1(ReportInfo):

    def __init__(self):
        super().initWithParams(
            name="SMBv1 Enabled",
            category="Systemhardening",
            tags=["Systemhardening", "SMB", "SMBv1"],
            description='Report all hosts where SMBv1 is installed / enabled.',
            views=[("view", url_for("sysinfo.hosts_report_smbv1"))]
        )