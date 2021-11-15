# Generated by Django 3.2.9 on 2021-11-08 08:30

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(default='', max_length=50, unique=True)),
                ('nickname', models.CharField(default='', max_length=100, unique=True)),
                ('name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=30)),
                ('department', models.CharField(choices=[('AI융합학부', 'AI융합학부'), ('가정교육과', '가정교육과'), ('건설환경공학과', '건설환경공학과'), ('건축공학부', '건축공학부'), ('경영정보학과', '경영정보학과'), ('경영학과', '경영학과'), ('경제학과', '경제학과'), ('경찰행정학부', '경찰행정학부'), ('광고홍보학과', '광고홍보학과'), ('교육학과', '교육학과'), ('국어교육과', '국어교육과'), ('국어국문학전공', '국어국문학전공'), ('국제통상학과', '국제통상학과'), ('글로벌무역학과', '글로벌무역학과'), ('기계로봇에너지공학과', '기계로봇에너지공학과'), ('멀티미디어공학과', '멀티미디어공학과'), ('문예창작학전공', '문예창작학전공'), ('물리학전공', '물리학전공'), ('뮤지컬전공', '뮤지컬전공'), ('미디어커뮤니케이션학전공', '미디어커뮤니케이션학전공'), ('바이오환경과학과', '바이오환경과학과'), ('반도체과학전공', '반도체과학전공'), ('법학과', '법학과'), ('북한학전공', '북한학전공'), ('불교미술전공', '불교미술전공'), ('불교학부', '불교학부'), ('사학과', '사학과'), ('사회복지상담학과', '사회복지상담학과'), ('사회복지학과', '사회복지학과'), ('사회학전공', '사회학전공'), ('산업시스템공학과', '산업시스템공학과'), ('생명과학과', '생명과학과'), ('서양화전공', '서양화전공'), ('수학과', '수학과'), ('수학교육과', '수학교육과'), ('스포츠문화학과', '스포츠문화학과'), ('식품산업관리학과', '식품산업관리학과'), ('식품생명공학과', '식품생명공학과'), ('약학과', '약학과'), ('역사교육과', '역사교육과'), ('연극전공', '연극전공'), ('영어문학전공', '영어문학전공'), ('영어통번역학전공', '영어통번역학전공'), ('영화영상학과', '영화영상학과'), ('윤리문화학전공', '윤리문화학전공'), ('융합보안학과', '융합보안학과'), ('융합에너지신소재공학과', '융합에너지신소재공학과'), ('의생명공학과', '의생명공학과'), ('일본학과', '일본학과'), ('전자전기공학부', '전자전기공학부'), ('정보통신공학전공', '정보통신공학전공'), ('정치외교학전공', '정치외교학전공'), ('조소전공', '조소전공'), ('중어중문학과', '중어중문학과'), ('지리교육과', '지리교육과'), ('철학과', '철학과'), ('체육교육과', '체육교육과'), ('컴퓨터공학전공', '컴퓨터공학전공'), ('통계학과', '통계학과'), ('한국화전공', '한국화전공'), ('행정학전공', '행정학전공'), ('화공생물공학과', '화공생물공학과'), ('화학과', '화학과'), ('회계학과', '회계학과')], default='', max_length=50)),
                ('school_id', models.CharField(default='', max_length=30)),
                ('is_dorm', models.CharField(default='', max_length=10)),
                ('dorm_id', models.CharField(default='', max_length=30)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('d_followings', models.ManyToManyField(related_name='d_followers', to=settings.AUTH_USER_MODEL)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('s_followings', models.ManyToManyField(related_name='s_followers', to=settings.AUTH_USER_MODEL)),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
