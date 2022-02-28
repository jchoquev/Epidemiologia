from email.policy import default
from django.db import models
import datetime

class tipoDocumento(models.Model):
    id=models.CharField(primary_key=True,unique=True,max_length=3)
    documento=models.CharField(max_length=50)

class TipoPrueba(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    nombre=models.CharField(max_length=50)

class TipoMuestra(models.Model):
    id=models.CharField(max_length=3, primary_key=True,unique=True)
    nombre=models.CharField(max_length=50)

class PacienteNetLab(models.Model):
    tdocumento=models.ForeignKey(tipoDocumento, on_delete=models.CASCADE)
    ndocumento=models.CharField(max_length=20)
    apePaterno=models.CharField(max_length=100,blank=True,null=True)
    apeMaterno=models.CharField(max_length=100,blank=True,null=True)
    nombres=models.CharField(max_length=100,blank=True,null=True)
    fobtencion=models.DateField(null=False)
    codOrden=models.CharField(max_length=20,blank=True,null=True)
    fobtencion=models.DateTimeField(blank=True,null=True)
    enfermedad=models.CharField(max_length=200,blank=True,null=True)
    componente=models.CharField(max_length=200,blank=True,null=True)
    resultado=models.CharField(max_length=200,blank=True,null=True)
    fpublicacionr=models.DateTimeField(blank=True,null=True)
    eessorigen=models.CharField(max_length=500,blank=True,null=True)
    estado=models.CharField(max_length=100,blank=True,null=True)
    revisado=models.BooleanField(default=False)
    tprueba=models.ForeignKey(TipoPrueba, on_delete=models.CASCADE)
    error=models.CharField(max_length=100,default='')
    createAt=models.DateTimeField(auto_now_add=True)
    updateAt=models.DateTimeField(auto_now=True)
    deleteAt=models.BooleanField(default=False)

class eess(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    iddiresa=models.CharField(max_length=3)
    diresa=models.CharField(max_length=100)
    idredes=models.CharField(max_length=3)
    redes=models.CharField(max_length=100)
    idmicrored=models.CharField(max_length=3)
    microred=models.CharField(max_length=100)
    ideess=models.CharField(max_length=10)
    eess=models.CharField(max_length=100)

class clasificacioncaso(models.Model):
    id=models.CharField(primary_key=True,unique=True,max_length=2)
    casoasig=models.CharField(max_length=50)

class tipovia(models.Model):
    id=models.CharField(primary_key=True,unique=True,max_length=3)
    viaasig=models.CharField(max_length=50)

class tipoCaso(models.Model):
    id=models.CharField(primary_key=True,unique=True,max_length=3)
    tcasoasig=models.CharField(max_length=50)

class resultado(models.Model):
    id=models.CharField(primary_key=True,unique=True,max_length=3)
    resutaldoasig=models.CharField(max_length=50)

class resultadodesc(models.Model):
    id=models.CharField(primary_key=True,unique=True,max_length=3)
    resutaldodescasig=models.CharField(max_length=50)

class perllenaficha(models.Model):
    id=models.CharField(primary_key=True,unique=True,max_length=3)
    perllenafichasig=models.CharField(max_length=200)

class tipovacuna(models.Model):
    idv=models.CharField(primary_key=True,max_length=4)
    nombre=models.CharField(max_length=100)
    pass

class NotiCovid(models.Model):
    id=models.AutoField(primary_key=True,unique=True)
    fnotificacion=models.DateField(null=True)
    eess=models.ForeignKey(eess, on_delete=models.CASCADE,blank=True,null=True)
    classcaso=models.ForeignKey(clasificacioncaso, on_delete=models.CASCADE,blank=True,null=True)
    tdocumento=models.ForeignKey(tipoDocumento, on_delete=models.CASCADE,blank=True,null=True)
    ndocumento=models.CharField(max_length=20)
    apeynombres=models.CharField(max_length=200)
    ncelular=models.CharField(max_length=20)
    peso=models.CharField(max_length=3)
    talla=models.CharField(max_length=3)
    tvia=models.ForeignKey(tipovia, on_delete=models.CASCADE,blank=True,null=True)
    npuerta=models.CharField(max_length=20)
    nombrevia=models.CharField(max_length=200)
    tcaso=models.ForeignKey(tipoCaso, on_delete=models.CASCADE,blank=True,null=True)
    finiciosintomas=models.DateField(blank=True,null=True)
    finiciosaislamiento=models.DateField(blank=True,null=True)
    sintomas=models.JSONField(blank=True,null=True)
    contactodir=models.JSONField(blank=True,null=True)
    vacuna1_fecha=models.DateField(blank=True,null=True)
    vacuna1_tipo=models.ForeignKey(tipovacuna,name="vacuna1_id",related_name="vacuna1_id", on_delete=models.CASCADE,blank=True,null=True)
    vacuna2_fecha=models.DateField(blank=True,null=True)
    vacuna2_tipo=models.ForeignKey(tipovacuna,name="vacuna2_id",related_name="vacuna2_id", on_delete=models.CASCADE,blank=True,null=True)
    vacuna3_fecha=models.DateField(blank=True,null=True)
    vacuna3_tipo=models.ForeignKey(tipovacuna,name="vacuna3_id",related_name="vacuna3_id", on_delete=models.CASCADE,blank=True,null=True)
    tprueba=models.ForeignKey(TipoPrueba, on_delete=models.CASCADE,blank=True,null=True)
    tmuestra=models.ForeignKey(TipoMuestra, on_delete=models.CASCADE,blank=True,null=True)
    ftmuestra=models.DateField(blank=True,null=True)
    tmuestra=models.ForeignKey(resultado, on_delete=models.CASCADE,blank=True,null=True)
    fresultado=models.DateField(blank=True,null=True)
    resultadodesc=models.ForeignKey(resultadodesc, on_delete=models.CASCADE,blank=True,null=True)
    perllenaficha=models.ForeignKey(perllenaficha, on_delete=models.CASCADE,blank=True,null=True)
    createAt=models.DateField(auto_now_add=True)
    UpdateAt=models.DateField(auto_now=True)
    deleteAt=models.BooleanField(default=False)
    

class vacunas(models.Model):
    ndocumento=models.CharField(max_length=20)
    apenombres=models.CharField(max_length=200,default='')
    fvacuna=models.DateField()
    ndosis=models.IntegerField()
    idfabricante=models.ForeignKey(tipovacuna, on_delete=models.CASCADE)

class vacunasf(models.Model):
    ndocumento=models.CharField(max_length=20)
    nombres=models.CharField(max_length=200)
    sexo=models.CharField(max_length=50)
    fnacimeinto=models.DateField(blank=True,null=True)
    fvacuna=models.DateField(blank=True,null=True)
    ndosis=models.IntegerField()
    vacuna=models.CharField(max_length=50)

class negativos(models.Model):
    nombres=models.CharField(max_length=200)
    edad=models.IntegerField()
    sexo=models.CharField(max_length=50)
    residactual=models.CharField(max_length=200)
    ftomamuestra=models.DateField(blank=True,null=True)
    ndocumento=models.CharField(max_length=20)
    telefono=models.CharField(max_length=15)
    microred=models.CharField(max_length=200)
    eess=models.CharField(max_length=200)
    vacccovid=models.CharField(max_length=4)
    f1sosis=models.DateField(blank=True,null=True)
    f2dosis=models.DateField(blank=True,null=True)
    tvacuna=models.CharField(max_length=50)
    f3dosis=models.DateField(blank=True,null=True)
    tvacuna2=models.CharField(max_length=50)
    createAt=models.DateTimeField(blank=True,null=True)
    updateAt=models.DateTimeField(blank=True,null=True,default=None)
    deleteAt=models.BooleanField(default=False,blank=True,null=True)

