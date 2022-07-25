from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *


class ArticleAdmin(ModelAdmin):
    list_display = ['id',
                    'ExternalId',
                    'SupplierId',
                    'AssemblyGroup',
                    'GenericArticle',
                    'ArticleNumber',
                    'Type',
                    'GenericArticleNumber',
                    ]
    search_fields = ['ArticleNumber', 'ExternalId']


class OemAdmin(ModelAdmin):
    list_display = ['id',
                    'Brand',
                    'OemNumber',
                    'ArticleId',
                    'IsOriginal',
                    'NormalizerOemNumber',
                    'IsReplacer'
                    ]
    search_fields = ['OemNumber', 'Brand']


class VehicleModelAdmin(ModelAdmin):
    list_display = ['id',
                    'VehicleBrandId',
                    'Name',
                    'ModelNumber'
                    ]
    search_fields = ['Name']


class VehicleBrandAdmin(ModelAdmin):
    list_display = ['id',
                    'Name',
                    ]
    search_fields = ['Name']


class VehiclesAdmin(ModelAdmin):
    list_display = ['id',
                    'VehicleModelId',
                    'TypeNumber',
                    'Year',
                    'BodyType',
                    'DriveType',
                    'EngineType',
                    'ValvesPerChamber',
                    'Cylinders',
                    'Volume',
                    'CcmTech',
                    'FuelType',
                    'FuelMixtureFormation',
                    'HorsePowers',
                    'KiloWatts',
                    'Engines',
                    'TypeName',
                    ]


class VehicleToArticleAdmin(ModelAdmin):
    list_display = ['id',
                    'ArticleId',
                    'VehicleId',
                    'Criterias',
                    'ExternalId',
                    ]
    search_fields = ['ExternalId']


class DisplayBraAdmin(ModelAdmin):
    list_display = ['id',
                    'bra_brand_no',
                    'bra_short_name',
                    'view_term_plain',
                    ]
    search_fields = ['bra_brand_no', 'bra_short_name', 'view_term_plain',]



admin.site.register(VehicleBrands, VehicleBrandAdmin)
admin.site.register(VehicleModels, VehicleModelAdmin)
admin.site.register(Vehicles, VehiclesAdmin)
admin.site.register(Suppliers)
admin.site.register(Articles, ArticleAdmin)
admin.site.register(File)
admin.site.register(ArticlesToVehicle, VehicleToArticleAdmin)
admin.site.register(ArticleOem, OemAdmin)
admin.site.register(Marketplaces)
admin.site.register(DisplayBra, DisplayBraAdmin)
