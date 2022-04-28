from django.http import FileResponse
from tempfile import NamedTemporaryFile
from string import ascii_uppercase as EN_ALPH
from openpyxl.styles import Font
import openpyxl as xls
from forms import models
from sesc.settings import SITE_URL


HEADER_FONT = Font(name='Times New Roman', size=14, bold=True)
SUBJ_NAMES = {
    "10 гум": {
        'd1': 'Второй иностранный язык (Б)',
        'd2': 'География (Б)',
        'd3': 'Обществознание (Б)',
        'd4': 'Теория познания (Б)',
        'd5': 'Информатика (Б)',
        'd6': 'Естествознание (Б)',
        'd7': 'Диалоги с Чеховым',
        'd8': 'Современная литература в жанровом аспекте',
        'd9': 'Риторика',
        'd10': 'История философии',
        'd11': 'История мировой культуры',
    },
    "10 соцгум": {
        'd1': 'География (Б)',
        'd2': 'Теория познания (Б)',
        'd3': 'МХК (Б)',
        'd4': 'Информатика (Б)',
        'd5': 'Естествознание (Б)',
        'd6': 'Зарубежная литература',
        'd7': 'Современная литература в жанровом аспекте',
        'd8': 'Диалоги с Чеховым',
        'd9': 'Политология',
        'd10': 'Социология',
        'd11': 'История философии',
    },
    "10 соцэк": {
        'd1': 'Теория познания (Б)',
        'd2': 'МХК (Б)',
        'd3': 'География (Б)',
        'd4': 'Информатика (Б)',
        'd5': 'Естествознание (Б)',
        'd6': 'Экономическая география',
        'd7': 'История философии',
        'd8': 'Сложные математические задачи',
    },
    '10 матинф': {
        'd1': 'Обществознание (Б)',
        'd2': 'География (Б)',
        'd3': 'МХК (Б)',
        'd4': 'Теория познания (Б)',
        'd5': 'Биология (Б)',
        'd6': 'Физика (Б)',
        'd7': 'Химия (Б)',
        'd8': 'Избранные главы учебников естественных наук',
    },
    '10 физмат': {
        'd1': 'Обществознание (Б)',
        'd2': 'География (Б)',
        'd3': 'МХК (Б)',
        'd4': 'Теория познания (Б)',
        'd5': 'Биология (Б)',
        'd6': 'Химия (Б)',
        'd7': 'Астрономия',
        'd8': 'Избранные главы учебников естественных наук',
    }
}


def export(request):
    BOOK = xls.Workbook()
    INFO = {
        '10 гум': {
            'd1': models.Gum.objects.filter(d1=True, attached=True),
            'd2': models.Gum.objects.filter(d2=True, attached=True),
            'd3': models.Gum.objects.filter(d3=True, attached=True),
            'd4': models.Gum.objects.filter(d4=True, attached=True),
            'd5': models.Gum.objects.filter(d5=True, attached=True),
            'd6': models.Gum.objects.filter(d6=True, attached=True),
            'd7': models.Gum.objects.filter(d7=True, attached=True),
            'd8': models.Gum.objects.filter(d8=True, attached=True),
            'd9': models.Gum.objects.filter(d9=True, attached=True),
            'd10': models.Gum.objects.filter(d10=True, attached=True),
            'd11': models.Gum.objects.filter(d11=True, attached=True),
        },
        '10 соцгум': {
            'd1': models.Sgum.objects.filter(d1=True, attached=True),
            'd2': models.Sgum.objects.filter(d2=True, attached=True),
            'd3': models.Sgum.objects.filter(d3=True, attached=True),
            'd4': models.Sgum.objects.filter(d4=True, attached=True),
            'd5': models.Sgum.objects.filter(d5=True, attached=True),
            'd6': models.Sgum.objects.filter(d6=True, attached=True),
            'd7': models.Sgum.objects.filter(d7=True, attached=True),
            'd8': models.Sgum.objects.filter(d8=True, attached=True),
            'd9': models.Sgum.objects.filter(d9=True, attached=True),
            'd10': models.Sgum.objects.filter(d10=True, attached=True),
            'd11': models.Sgum.objects.filter(d11=True, attached=True),
        },
        '10 соцэк': {
            'd1': models.SocEk.objects.filter(d1=True, attached=True),
            'd2': models.SocEk.objects.filter(d2=True, attached=True),
            'd3': models.SocEk.objects.filter(d3=True, attached=True),
            'd4': models.SocEk.objects.filter(d4=True, attached=True),
            'd5': models.SocEk.objects.filter(d5=True, attached=True),
            'd6': models.SocEk.objects.filter(d6=True, attached=True),
            'd7': models.SocEk.objects.filter(d7=True, attached=True),
            'd8': models.SocEk.objects.filter(d8=True, attached=True),
        },
        '10 матинф': {
            'd1': models.MatInf.objects.filter(d1=True, attached=True),
            'd2': models.MatInf.objects.filter(d2=True, attached=True),
            'd3': models.MatInf.objects.filter(d3=True, attached=True),
            'd4': models.MatInf.objects.filter(d4=True, attached=True),
            'd5': models.MatInf.objects.filter(d5=True, attached=True),
            'd6': models.MatInf.objects.filter(d6=True, attached=True),
            'd7': models.MatInf.objects.filter(d7=True, attached=True),
            'd8': models.MatInf.objects.filter(d8=True, attached=True),
        },
        '10 физмат': {
            'd1': models.FizMat.objects.filter(d1=True, attached=True),
            'd2': models.FizMat.objects.filter(d2=True, attached=True),
            'd3': models.FizMat.objects.filter(d3=True, attached=True),
            'd4': models.FizMat.objects.filter(d4=True, attached=True),
            'd5': models.FizMat.objects.filter(d5=True, attached=True),
            'd6': models.FizMat.objects.filter(d6=True, attached=True),
            'd7': models.FizMat.objects.filter(d7=True, attached=True),
            'd8': models.FizMat.objects.filter(d8=True, attached=True),
        }
    }

    for form_ind, form in enumerate(INFO):
        sheet = BOOK.create_sheet(index=0, title=form)
        for subj_ind, subj in enumerate(INFO[form]):
            sheet.cell(1, subj_ind + 1, SUBJ_NAMES[form][subj]).font = HEADER_FONT
            sheet.cell(2, subj_ind + 1, len(INFO[form][subj])).font = HEADER_FONT
            sheet.column_dimensions[EN_ALPH[subj_ind % len(EN_ALPH)]].width = 45
            for stud_ind in range(len(INFO[form][subj])):  #* ФИО обучающихся & URL
                hyperlink = f'{SITE_URL}/{form_ind + 1}/{INFO[form][subj][stud_ind].slug}'
                sheet.cell(stud_ind + 3, subj_ind + 1, f'{INFO[form][subj][stud_ind]}')
                sheet.cell(stud_ind + 3, subj_ind + 1).hyperlink = hyperlink
    book_file = NamedTemporaryFile(prefix='', suffix='.xlsx')
    BOOK.save(book_file.name)
    export_response = FileResponse(open(book_file.name, 'rb'), as_attachment=True)
    book_file.close()
    return export_response
