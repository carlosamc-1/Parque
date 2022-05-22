# Generated by Django 4.0.2 on 2022-03-10 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('parque', '0002_alter_cliente_nib'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrador',
            name='parqueid',
            field=models.ForeignKey(db_column='ParqueID', on_delete=django.db.models.deletion.CASCADE, to='parque.parque'),
        ),
        migrations.AlterField(
            model_name='contrato',
            name='clienteid',
            field=models.ForeignKey(db_column='ClienteID', on_delete=django.db.models.deletion.CASCADE, to='parque.cliente'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='parqueid',
            field=models.ForeignKey(db_column='ParqueID', on_delete=django.db.models.deletion.CASCADE, to='parque.parque'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='contratoid',
            field=models.ForeignKey(db_column='ContratoID', on_delete=django.db.models.deletion.CASCADE, to='parque.contrato'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='reservaid',
            field=models.ForeignKey(db_column='ReservaID', on_delete=django.db.models.deletion.CASCADE, to='parque.reserva'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='viaturaid',
            field=models.ForeignKey(db_column='ViaturaID', on_delete=django.db.models.deletion.CASCADE, to='parque.viatura'),
        ),
        migrations.AlterField(
            model_name='lugar',
            name='zonaid',
            field=models.ForeignKey(db_column='ZonaID', on_delete=django.db.models.deletion.CASCADE, to='parque.zona'),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='contratoid',
            field=models.ForeignKey(db_column='ContratoID', on_delete=django.db.models.deletion.CASCADE, to='parque.contrato'),
        ),
        migrations.AlterField(
            model_name='tabelaprecos',
            name='parqueid',
            field=models.ForeignKey(db_column='ParqueID', on_delete=django.db.models.deletion.CASCADE, to='parque.parque'),
        ),
        migrations.AlterField(
            model_name='viatura',
            name='contratoid',
            field=models.ForeignKey(db_column='ContratoID', on_delete=django.db.models.deletion.CASCADE, to='parque.contrato'),
        ),
        migrations.AlterField(
            model_name='viatura',
            name='registo_movimentoid',
            field=models.ForeignKey(db_column='Registo-movimentoID', on_delete=django.db.models.deletion.CASCADE, to='parque.registomovimento'),
        ),
        migrations.AlterField(
            model_name='zona',
            name='parqueid',
            field=models.ForeignKey(db_column='ParqueID', on_delete=django.db.models.deletion.CASCADE, to='parque.parque'),
        ),
    ]