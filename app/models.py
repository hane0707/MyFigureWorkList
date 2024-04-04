from django.db import models

class Material(models.Model):
    class Meta:
        db_table = 'material'
    
    name = models.CharField(verbose_name='素材', max_length=100)
    
    def __str__(self):
        return self.name
    
class Work(models.Model):
    class Meta:
        db_table = 'work'
    
    name = models.CharField(verbose_name='作品名', max_length=100)

    def __str__(self):
        return self.name
    
class Character(models.Model):
    class Meta:
        db_table = 'character'
    
    name = models.CharField(verbose_name='キャラクター名称', max_length=100)
    work = models.ForeignKey(Work, verbose_name='作品名称', on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
class Figure(models.Model):
    class Meta:
        db_table = 'figure'
    
    name = models.CharField(verbose_name='名称', max_length=20)
    create_date = models.DateField(verbose_name='完成日')
    materials = models.ManyToManyField(Material, verbose_name='素材')
    motif = models.ForeignKey(Character, verbose_name='キャラクターモチーフ', on_delete=models.PROTECT)

    def __str__(self):
        return self.name

