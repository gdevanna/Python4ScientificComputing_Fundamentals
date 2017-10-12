# -*- coding: utf-8 -*-
material_library={"outside_surface_winter":0.030,"outside_surface_summer":0.044,"wood_bevel":0.14,
"wood_fiberboard":0.23,"glass_fiber":2.45,"wood_stud":0.63,"glass_fiber":2.45,"inside_surface":0.12,
"gypsum_wallboard":0.079}

instuds=["wood_bevel","wood_fiberboard","gypsum_wallboard"]
atstuds=["glass_fiber","wood_stud"]
air=["outside_surface_winter","inside_surface"]
series=instuds+air
glassparallel=float(0.75)
studsparallel=float(0.25)

#RESISTENCE

Rserietot=0
Rvalues_layer=[]
for anymaterial in series:
    Rvalue_layer = material_library[anymaterial]
    Rserietot= Rserietot+Rvalue_layer
    Rvalues_layer.append(Rvalues_layer)

print"the value of resistence for this layer is: "+str(Rvalues_layer)    
print"the toatal resistence in series is "+str(Rserietot)+"m^2*°C/W"

#parallel

Rtotpara=0
for anymaterial in atstuds:
    Rvalue_layer = material_library[anymaterial]
    Rtotpara=Rtotpara+1/Rvalue_layer
print"the toatal resistence in parallel is "+str(Rtotpara)+"m^2*°C/W"
    
#air
Rtotair=0
for anymaterial in air:
    Rvalue_layer = material_library[anymaterial]
    Rtotair=Rtotair+Rvalue_layer
print"the toatal resistence due to the air is "+str(Rtotair)+"m^2*°C/W"
    
Rtot=Rtotair+Rtotpara+Rserietot
print"the toatal resistence is "+str(Rtot)+"m^2*°C/W"
Utot=1/Rtot
print"the toatal U is "+str(Utot)