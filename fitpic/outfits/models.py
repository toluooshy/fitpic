from django.db import models

# MODELS:

clothingCategories = (
    ('TOPS', 'Tops (shirts, sweaters, jackets,...)'),
    ('BTTM', 'Bottoms (shorts, pants, skirts,...)'),
    ('FTGR', 'Footgear (shoes, boots, sandals,...)'),
    ('HDGR', 'Headgear (glasses, hats, facial piercings,...)'),
    ('ACCS', 'Accessories (jewelry, belts, watches,...)'),
)

class Clothing(models.Model):
    title = models.CharField(max_length=50)
    category = models.CharField(max_length=4, choices=clothingCategories, default='TOPS')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
