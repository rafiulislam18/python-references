from django.db import models
from django.utils import timezone
from django.utils.text import slugify


class DrugClass(models.Model):
    drug_class_id = models.IntegerField(verbose_name="Drug Class ID", max_length=50, unique=True)
    drug_class_name = models.CharField(verbose_name="Drug Class Name", max_length=100)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    generics_count = models.IntegerField(default=0)

    def __str__(self):
        return self.drug_class_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.drug_class_name}-{self.drug_class_id}")
        super().save(*args, **kwargs)


class DrugSubclass(models.Model):
    name = models.CharField(max_length=100)
    parent_drug = models.ForeignKey(DrugClass, on_delete=models.CASCADE)
    parent_subclass = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    related_medicine = models.ManyToManyField('BrandName', blank=True)

    def str(self):
        return self.name
    

class Indication(models.Model):
    indication_id = models.IntegerField(verbose_name="Indication ID", max_length=50, unique=True)
    indication_name = models.CharField(verbose_name="Indication Name", max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    generics_count = models.IntegerField(default=0)

    def __str__(self):
        return self.indication_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.indication_name}-{self.indication_id}")
        super().save(*args, **kwargs)


class DosageForm(models.Model):
    dosage_form_id = models.IntegerField(verbose_name="Dosage Form ID", max_length=50, unique=True)
    dosage_form_name = models.CharField(verbose_name="Dosage Form Name", max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    brand_names_count = models.IntegerField(default=0)

    def __str__(self):
        return self.dosage_form_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.dosage_form_name}-{self.dosage_form_id}")
        super().save(*args, **kwargs)


class Manufacturer(models.Model):
    manufacturer_id = models.IntegerField(verbose_name="Manufacturer ID", max_length=50, unique=True)
    manufacturer_name = models.CharField(verbose_name="Manufacturer Name", max_length=255)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    generics_count = models.IntegerField(default=0)
    brand_names_count = models.IntegerField(default=0)

    def __str__(self):
        return self.manufacturer_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.manufacturer_name}-{self.manufacturer_id}")
        super().save(*args, **kwargs)
    

class Generic(models.Model):
    generic_id = models.IntegerField(verbose_name="Generic ID", max_length=50, unique=True)
    generic_name = models.CharField(verbose_name="Generic Name", max_length=50)
    slug = models.SlugField(max_length=50, unique=True, blank=True)
    monagraph_link = models.URLField(max_length=500, blank=True, null=True)
    drug_class = models.ForeignKey(DrugClass, on_delete=models.SET_NULL, null=True, blank=True)
    indication = models.ForeignKey(Indication, on_delete=models.SET_NULL, null=True, blank=True)
    indication_description = models.TextField(null=True, blank=True)
    therapeutic_class_description = models.TextField(null=True, blank=True)
    pharmacology_description = models.TextField(null=True, blank=True)
    dosage_description = models.TextField(null=True, blank=True)
    administration_description = models.TextField(null=True, blank=True)
    interaction_description = models.TextField(null=True, blank=True)
    contraindicaions_description = models.TextField(null=True, blank=True)
    side_effects_description = models.TextField(null=True, blank=True)
    pregnancy_and_lactation_description = models.TextField(null=True, blank=True)
    precautions_description = models.TextField(null=True, blank=True)
    pediatric_description = models.TextField(null=True, blank=True)
    overdose_effects_description = models.TextField(null=True, blank=True)
    duration_of_treatment_description = models.TextField(null=True, blank=True)
    reconsitution_description = models.TextField(null=True, blank=True)
    storage_conditions_description = models.TextField(null=True, blank=True)
    description_count = models.IntegerField(default=0)
    # sub_drug_class = models.ForeignKey(DrugSubclass, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.generic_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.generic_name}-{self.generic_id}")
        super().save(*args, **kwargs)


class Medicine(models.Model):
    brand_id = models.IntegerField(verbose_name="Brand ID", max_length=50, unique=True)
    brand_name = models.CharField(verbose_name="Brand Name", max_length=255)
    brand_type = models.CharField(verbose_name="Brand Type", max_length=50, blank=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    dosage_form = models.ForeignKey(DosageForm, on_delete=models.SET_NULL, null=True, blank=True)
    generic = models.ForeignKey(Generic, on_delete=models.SET_NULL, null=True, blank=True)
    strength = models.CharField(max_length=100, blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.SET_NULL, null=True, blank=True)
    package_container = models.CharField(max_length=255, blank=True, null=True)
    package_size = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.brand_name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.brand_name}-{self.brand_id}")
        super().save(*args, **kwargs)


# class DrugClass(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name


# class SubDrugClass(models.Model):
#     name = models.CharField(max_length=100)
#     drug_class = models.ForeignKey(DrugClass, on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return self.name


# class CommonQuestion(models.Model):
#     question = models.CharField(verbose_name="Question", max_length=255)
#     answer = models.TextField(verbose_name="Answer")
#     medicine = models.ForeignKey(BrandName, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.question
    

# class QuickTip(models.Model):
#     tips = models.CharField(verbose_name="Tips", max_length=255)
#     medicine = models.ForeignKey(BrandName, on_delete=models.CASCADE)

#     def __str__(self):
#         return self.tips