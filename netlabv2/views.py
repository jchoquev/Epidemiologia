#from distutils.log import error
#from multiprocessing import context
from tokenize import group
from tracemalloc import start
from django.shortcuts import render
#from django.template import Template, Context
#from django.core import serializers
#from django.http import HttpResponse
from django.http import JsonResponse
from netlabv2.models import PacienteNetLab,tipoDocumento,TipoPrueba,vacunasf,negativos,eess
from netlabv2.functions import agregarCabecera
from django.views.decorators.csrf import csrf_exempt
from datetime import timedelta
#from netlabv2.models_conn import JoinPacienteNetLab
from django.db import connection
import datetime

# Create your views here.
def netlav2(request):
    tdocumento=tipoDocumento.objects.raw("SELECT * FROM netlabv2_tipodocumento")
    tipoprueba=TipoPrueba.objects.raw("SELECT * FROM netlabv2_tipoprueba")
    return render(request,"ingresodatos.html",{'tdocumento':tdocumento,'tipoprueba':tipoprueba,})

def guadardatosini(request):
    data=PacienteNetLab(tdocumento_id=tipoDocumento.objects.get(id=request.GET['input_tdocumento']),
                        ndocumento=request.GET['input__dni'],
                        fobtencion=request.GET['input__fobtencion'],
                        tprueba_id=TipoPrueba.objects.get(id=request.GET['input__tprueba']),
                        createAt=datetime.datetime.now(), )
    data.save()
    return JsonResponse({'msg': 'ok'})

def dtablePacientesNetLab(request):
    #cursor.execute("SELECT * FROM usuarios")
    #JoinPacienteNetLab
    sqli=''' SELECT lab.id, td.id as iddocumento,
        td.documento as documento, lab.ndocumento,lab.fobtencion,
        lab.revisado,tp.id as idtprueba, tp.nombre as tprueba,
        lab.error,lab.createAt
        from netlabv2_pacientenetlab lab
        INNER JOIN netlabv2_tipodocumento td  ON lab.tdocumento_id=td.id
        INNER join netlabv2_tipoprueba tp on lab.tprueba_id=tp.id '''
    ordenar='ORDER BY lab.id ASC'
    wfecha=''
    wrevisado=''
    if request.GET.get('ordenarID','')=='true':
        ordenar=" ORDER BY lab.id DESC "
    if request.GET['desde'] and request.GET['hasta']:
        wfecha="AND ( date(lab.createAt)>=date('{desde}') AND date(lab.createAt)<=date('{hasta}') )"
        wfecha=wfecha.format(desde=request.GET['desde'],hasta=request.GET['hasta'])
    if int(request.GET['revisado'])==2:
        wrevisado='AND lab.revisado=true'
    elif int(request.GET['revisado'])==3:
        wrevisado='AND lab.revisado=false'
    sql=sqli+" WHERE lab.ndocumento LIKE '%{search}%' {wfecha} {wrevisado}  AND lab.deleteAt=false {ordenar} LIMIT {start},{length}"
    sql=sql.format(wfecha=wfecha,wrevisado=wrevisado,search=request.GET.get('search[value]', ''),ordenar=ordenar,start=request.GET['start'], length=request.GET['length']) 

    sqlt=sqli+" WHERE lab.ndocumento LIKE '%{search}%' {wrevisado} {wfecha} AND lab.deleteAt=false "
    sqlt=sqlt.format(search=request.GET.get('search[value]', ''),wfecha=wfecha,wrevisado=wrevisado)
    with connection.cursor() as cursor:
        total=agregarCabecera(cursor.execute(sqlt))
        lista=agregarCabecera(cursor.execute(sql))

    return JsonResponse({"draw": request.GET['draw'],'ver':sql, "recordsTotal": request.GET['length'],"recordsFiltered": len(total),'data':lista}, safe=False)

def buscar_vacunado(request):
    data=vacunasf.objects.all().filter(ndocumento=request.GET.get("ndocumento",""))
    data=data.values()
    return JsonResponse({"msg":list(data)}, safe=False)

@csrf_exempt
def guardar_negativos(request):
    data = negativos(
        nombres=request.POST.get("nombres","").upper(),
        edad=request.POST.get("edad","").upper(),
        sexo=request.POST.get("sexo","").upper(),
        residactual=request.POST.get("resid_actual","").upper(),
        ftomamuestra=request.POST.get("fnotificacion","").upper(),
        ndocumento=request.POST.get("find_ndocumento","").upper(),
        telefono=request.POST.get("telefono","").upper(),
        microred=request.POST.get("microred","").upper(),
        eess=request.POST.get("eess","").upper(),
        vacccovid=request.POST.get("vac_covid","").upper(),
        tvacuna=request.POST.get("pvacuna","").upper(),
        tvacuna2=request.POST.get("tvacuna","").upper(),
        createAt=datetime.datetime.now(),
        updateAt=datetime.datetime.now())
    if request.POST.get("f1dosis")!="":
        data.f1sosis=request.POST.get("f1dosis")
    if request.POST.get("f2dosis")!="":
        data.f2dosis=request.POST.get("f2dosis")
    if request.POST.get("f3dosis")!="":
        data.f3dosis=request.POST.get("f3dosis")
    data.save()
    return JsonResponse({'msg': 'ok','accion':'insert'})

def lista_eess(request):
    tamaño=10
    page=int(request.GET.get('page'))
    start=0
    end=tamaño
    if page>0:
        start=page*tamaño-1
        end=page*tamaño+tamaño
    data=eess.objects.filter(eess__contains=request.GET.get('name'))[start:end].values()
    return JsonResponse({'msg': 'ok','data':list(data),'total':len(data)}, safe=False)

@csrf_exempt
def actualizar_negativos(request):
    data= negativos.objects.get(id=request.POST.get("hidden__input_id"))
    data.nombres=request.POST.get("nombres","").upper()
    data.edad=request.POST.get("edad","").upper()
    data.sexo=request.POST.get("sexo","").upper()
    data.residactual=request.POST.get("resid_actual","").upper()
    data.ftomamuestra=request.POST.get("fnotificacion","").upper()
    data.ndocumento=request.POST.get("find_ndocumento","").upper()
    data.telefono=request.POST.get("telefono","").upper()
    data.microred=request.POST.get("microred","").upper()
    data.eess=request.POST.get("eess","").upper()
    data.vacccovid=request.POST.get("vac_covid","").upper()
    data.tvacuna=request.POST.get("pvacuna","").upper()
    data.tvacuna2=request.POST.get("tvacuna","").upper()
    data.updateAt=datetime.datetime.now()
    if request.POST.get("f1dosis")!="":
        data.f1sosis=request.POST.get("f1dosis")
    if request.POST.get("f2dosis")!="":
        data.f2dosis=request.POST.get("f2dosis")
    if request.POST.get("f3dosis")!="":
        data.f3dosis=request.POST.get("f3dosis")

    data.save()
    return JsonResponse({'msg': 'ok','accion':'update'})

def listar_negativos(request):
    sqli='select * from netlabv2_negativos'
    wfecha=''
    wrevisado=''
    wlimit=''
    ordenar=''
    wwhere=("WHERE (ndocumento LIKE '%{search}%' OR nombres LIKE '%{search}%')").format(search=request.GET.get('search[value]', ''))
    if int(request.GET.get('desde'))>0:
        wwhere+=(" AND id>={desde}").format(desde=request.GET.get('desde'))
    if int(request.GET.get('hasta'))>0:
        wwhere+=(" AND id<={hasta}").format(hasta=request.GET.get('hasta')) 
    if request.GET.get('fnotificacion'):
        wwhere+=(" AND ftomamuestra=date('{fnotificacion}')").format(fnotificacion=request.GET.get('fnotificacion')) 
    if request.GET.get('eess'):
        wwhere+=(" AND eess LIKE '%{eess}%'").format(eess=request.GET.get('eess')) 
    if int(request.GET.get('length'))>0:
        wlimit="LIMIT {start},{length}"
        wlimit=wlimit.format(start=request.GET.get('start'), length=request.GET.get('length'))
    if request.GET.get('ordenarID','')=='true':
        ordenar="ORDER BY id DESC"
    sqlt=sqli+" {wwhere}"
    sqlt=sqlt.format(wwhere=wwhere)
    sqli='select * from netlabv2_negativos'+" {wwhere} {ordenar} {wlimit}"
    sqli=sqli.format(wlimit=wlimit,ordenar=ordenar,wwhere=wwhere)
    with connection.cursor() as cursor:
        total=agregarCabecera(cursor.execute(sqlt))
        lista=agregarCabecera(cursor.execute(sqli))
    return JsonResponse({"draw": request.GET['draw'], "recordsTotal": len(lista),"recordsFiltered": len(total),'data':lista}, safe=False)

def resumen__negativos(request):
    select='ftomamuestra'
    groupby=''
    orderby=''
    if int(request.GET.get('agrupar'))==1:
        select="microred,eess,ftomamuestra,NULL AS fingreso"
        groupby='group by microred,eess,ftomamuestra'
        orderby='ORDER BY ftomamuestra DESC'
    elif int(request.GET.get('agrupar'))==2:#micro red
        select='microred,NULL AS eess,NULL AS ftomamuestra,NULL AS fingreso'
        groupby='group by microred'
        orderby='ORDER BY microred ASC'
    elif int(request.GET.get('agrupar'))==3:#EESS
        select='microred,eess,NULL AS ftomamuestra,NULL AS fingreso'
        groupby='group by microred,eess'
        orderby='ORDER BY eess ASC'
    elif int(request.GET.get('agrupar'))==4:
        select='NULL AS microred,NULL AS eess,NULL AS ftomamuestra,date(createAt) AS fingreso'
        groupby='group by date(createAt)'
        orderby='ORDER BY date(createAt) DESC'
    sqli=('SELECT {select},count(*) AS contador FROM netlabv2_negativos WHERE (deleteAt=FALSE)').format(select=select)
    wwhere=''
    if request.GET.get('desde'):
        wwhere+=(" AND DATE(createAt)>='{desde}'").format(desde=request.GET.get('desde'))
    if request.GET.get('hasta'):
        wwhere+=(" AND DATE(createAt)<='{hasta}'").format(hasta=request.GET.get('hasta')) 
    if request.GET.get('fnotificacion'):
        wwhere+=(" AND ftomamuestra=date('{fnotificacion}')").format(fnotificacion=request.GET.get('fnotificacion'))
    if request.GET.get('eess'):
        wwhere+=(" AND eess LIKE '%{eess}%'").format(eess=request.GET.get('eess')) 
    
    sqli=(sqli+' {wwhere} {groupby} {orderby}').format(wwhere=wwhere,groupby=groupby,orderby=orderby)
    lista=agregarCabecera(connection.cursor().execute(sqli))
    return JsonResponse({'data':lista}, safe=False)
