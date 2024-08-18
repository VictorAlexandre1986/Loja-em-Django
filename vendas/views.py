from django.shortcuts import render
import io
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from xhtml2pdf import pisa
from rest_framework import viewsets
from .models import Venda
from .serializers import VendaSerializer


from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph



class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class VendaRelatorioView(APIView):

    def get(self, request, *args, **kwargs):
        vendas = Venda.objects.all()

        # Filtros
        data_inicio = request.query_params.get('data_inicio')
        data_fim = request.query_params.get('data_fim')
        vendedor_id = request.query_params.get('vendedor')
        cliente_id = request.query_params.get('cliente')

        if data_inicio and data_fim:
            vendas = vendas.filter(data__range=[data_inicio, data_fim])

        if vendedor_id:
            vendas = vendas.filter(vendedor_id=vendedor_id)

        if cliente_id:
            vendas = vendas.filter(cliente_id=cliente_id)

        export_type = request.query_params.get('export', 'json')

        if export_type == 'pdf':
            return self.export_pdf(vendas)
        elif export_type == 'excel':
            return self.export_excel(vendas)

        # Serializar os dados para JSON como padrão
        serializer = VendaSerializer(vendas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def export_pdf(self, vendas):
        buffer = io.BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=A4)

        elements = []

        # Estilo de Título
        styles = getSampleStyleSheet()
        title_style = styles['Heading1']
        title_style.alignment = TA_CENTER
        title = Paragraph("RELATÓRIO DE VENDAS", title_style)
        elements.append(title)

        data = [
            ["Venda ID", "Cliente", "Vendedor", "Data", "Produto", "Quantidade", "Preço Unitário (R$)", "Total (R$)"]]

        total_vendas_geral = 0

        for venda in vendas:
            for item in venda.itens.all():
                total_venda = item.quantidade * item.preco_unitario
                total_vendas_geral += total_venda
                data.append([
                    venda.id,
                    venda.cliente.nome,
                    venda.vendedor.nome,
                    venda.data.strftime('%d/%m/%Y'),
                    item.produto.nome,
                    item.quantidade,
                    f"{item.preco_unitario:.2f}",
                    f"{total_venda:.2f}"
                ])

        # Adiciona uma linha com o total geral das vendas
        data.append(["", "", "", "", "", "", "Total Geral:", f"R$ {total_vendas_geral:.2f}"])

        # Cria a tabela
        table = Table(data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        elements.append(table)

        # Constrói o PDF
        doc.build(elements)

        buffer.seek(0)
        return HttpResponse(buffer, content_type='application/pdf')
    def export_excel(self, vendas):
        data = []
        for venda in vendas:
            for item in venda.itens.all():
                data.append({
                    'Venda ID': venda.id,
                    'Data': venda.data.strftime('%d/%m/%Y'),
                    'Cliente': venda.cliente.nome,
                    'Vendedor': venda.vendedor.nome,
                    'Produto': item.produto.nome,
                    'Quantidade': item.quantidade,
                    'Preço Unitário': item.preco_unitario,
                    'Preço Total': item.quantidade * item.preco_unitario,
                })

        df = pd.DataFrame(data)

        buffer = io.BytesIO()
        with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
            df.to_excel(writer, index=False)

        buffer.seek(0)
        return HttpResponse(buffer, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', headers={'Content-Disposition': 'attachment; filename="relatorio_vendas.xlsx"'})