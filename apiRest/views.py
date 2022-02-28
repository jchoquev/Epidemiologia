from rest_framework.views import APIView
from rest_framework.response import Response
from netlabv2.functions import agregarCabecera
from django.db import connection

class helloapiView(APIView):
    def get(self,request,format=None):
        #if len(request.GET.get('asc'))>0&len(request.GET.get('asc'))>0&len(request.GET.get('asc'))>0:
        sqli=''' SELECT lab.ndocumento,strftime('%d/%m/%Y',date(lab.fobtencion)) as fobtencion
        from netlabv2_pacientenetlab lab
        INNER JOIN netlabv2_tipodocumento td  ON lab.tdocumento_id=td.id
        INNER join netlabv2_tipoprueba tp on lab.tprueba_id=tp.id '''
        ordenar='ORDER BY lab.id ASC'
        wfecha=''
        if request.GET.get('asc','')=='true':
            ordenar=" ORDER BY lab.id DESC "
        if request.GET['desde'] and request.GET['hasta']:
            wfecha="( date(lab.createAt)>=date('{desde}') AND date(lab.createAt)<=date('{hasta}') )"
            wfecha=wfecha.format(desde=request.GET['desde'],hasta=request.GET['hasta'])
        sqlt=sqli+" WHERE {wfecha} AND lab.revisado=false AND lab.deleteAt=false {ordenar}"
        sqlt=sqlt.format(wfecha=wfecha,ordenar=ordenar)
        lista=agregarCabecera(connection.cursor().execute(sqlt))
        an_apiview=['holas','mundo',request.GET.get('asc')]
        return Response({'message':True,'lista':lista})

