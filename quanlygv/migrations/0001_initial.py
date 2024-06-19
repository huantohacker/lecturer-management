# Generated by Django 4.1.7 on 2023-03-29 07:33

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('tai_khoan', models.CharField(max_length=20)),  
                ('mat_khau', models.CharField(max_length=20)), 
                ('ho_va_ten', models.CharField(max_length=50)), 
                ('dia_chi', models.CharField(max_length=128)), 
                ('sdt', models.CharField(max_length=10)), 
                ('anh', models.CharField(max_length=255)), 
            ],
        ), 
        migrations.CreateModel(
            name='Khoa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('ma_khoa', models.CharField(max_length=20)),  
                ('ten_khoa', models.CharField(max_length=128)), 
            ],
        ), 
        migrations.CreateModel(
            name='Monhoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('ma_mh', models.CharField(max_length=20)),  
                ('ten_mh', models.CharField(max_length=128)), 
                ('so_tc', models.PositiveIntegerField()), 
            ],
        ),
        migrations.CreateModel(
            name='Lophoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('ma_lop', models.CharField(max_length=20)),
                ('ten_lop', models.CharField(max_length=128)),
                ('si_so', models.PositiveIntegerField()),
                ('khoa', models.ForeignKey(to='quanlygv.Khoa', on_delete=django.db.models.deletion.CASCADE)), 
            ],
        ),
        migrations.CreateModel(
            name='Giangvien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('ho_ten_gv', models.CharField(max_length=50)),
                ('hoc_vi', models.CharField(max_length=128)),
                ('chuyen_mon', models.CharField(max_length=128)),
                ('chuc_vu', models.CharField(max_length=128)),
                ('ngay_sinh', models.CharField(max_length=50)),
                ('gioi_tinh', models.CharField(max_length=50)),
                ('sdt', models.CharField(max_length=10)),
                ('anh', models.CharField(max_length=255)),
                ('khoa', models.ForeignKey(to='quanlygv.Khoa', on_delete=django.db.models.deletion.CASCADE)), 
            ],
        ),
        migrations.CreateModel(
            name='Taikhoangv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('tai_khoan', models.CharField(max_length=20)),
                ('mat_khau', models.CharField(max_length=20)),
                ('giangvien', models.ForeignKey(to='quanlygv.Giangvien', on_delete=django.db.models.deletion.CASCADE)), 
            ],
        ),
        migrations.CreateModel(
            name='Phanconggv',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='id')),
                ('lophoc', models.ForeignKey(to='quanlygv.Lophoc', on_delete=django.db.models.deletion.CASCADE)),
                ('giangvien', models.ForeignKey(to='quanlygv.Giangvien', on_delete=django.db.models.deletion.CASCADE)),
                ('monhoc', models.ForeignKey(to='quanlygv.Monhoc', on_delete=django.db.models.deletion.CASCADE)),
                ('ngay_bd', models.DateField()),
                ('ngay_kt', models.DateField()),
                ('trang_thai', models.CharField(max_length=50)),
            ],
        ),
    ]
