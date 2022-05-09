from forms import models


def get_subjects():
    return {
        'ГУМ': (
            (
                {
                    'Второй иностранный язык (Б)': models.Gum.objects.filter(d1=True),
                    'География (Б)': models.Gum.objects.filter(d2=True),
                    'Обществознание (Б)': models.Gum.objects.filter(d3=True),
                    'Теория познания (Б)': models.Gum.objects.filter(d4=True),
                    'Информатика (Б)': models.Gum.objects.filter(d5=True),
                    'Естествознание (Б)': models.Gum.objects.filter(d6=True),
                },
                {
                    'Зарубежная литература': 1,
                    'Диалоги с Чеховым': models.Gum.objects.filter(d7=True),
                    'Современная литература в жанровом аспекте': models.Gum.objects.filter(d8=True),
                    'Риторика': models.Gum.objects.filter(d9=True),
                    'Сложные аспекты истории России c древнейших времен до конца XIX века': 1,
                    'История философии': models.Gum.objects.filter(d10=True),
                    'История мировой культуры': models.Gum.objects.filter(d11=True),
                },
            ),
            models.Gum.objects.all()
        ),
        'СГУМ': (
            (
                {
                    'География (Б)': models.Sgum.objects.filter(d1=True),
                    'Теория познания (Б)': models.Sgum.objects.filter(d2=True),
                    'МХК (Б)': models.Sgum.objects.filter(d3=True),
                    'Информатика (Б)': models.Sgum.objects.filter(d4=True),
                    'Естествознание (Б)': models.Sgum.objects.filter(d5=True),
                },
                {
                    'Риторика': 1,
                    'Зарубежная литература': models.Sgum.objects.filter(d6=True),
                    'Современная литература в жанровом аспекте': models.Sgum.objects.filter(d7=True),
                    'Диалоги с Чеховым': models.Sgum.objects.filter(d8=True),
                    'Сложные аспекты истории России c древнейших времен до конца XIX века': 1,
                    'Политология': models.Sgum.objects.filter(d9=True),
                    'Социология': models.Sgum.objects.filter(d10=True),
                    'История философии': models.Sgum.objects.filter(d11=True),
                },
            ),
            models.Sgum.objects.all()
        ),
        'СОЦЭК': (
            (
                {
                    'Теория познания (Б)': models.SocEk.objects.filter(d1=True),
                    'МХК (Б)': models.SocEk.objects.filter(d2=True),
                    'География (Б)': models.SocEk.objects.filter(d3=True),
                    'Информатика (Б)': models.SocEk.objects.filter(d4=True),
                    'Естествознание (Б)': models.SocEk.objects.filter(d5=True),
                },
                {
                    'Экономическая география': models.SocEk.objects.filter(d6=True),
                    'Экономические задачи повышенной сложности': 1,
                    'История философии': models.SocEk.objects.filter(d7=True),
                    'Сложные математические задачи': models.SocEk.objects.filter(d8=True),
                }
            ),
            models.SocEk.objects.all()
        ),
        'МИ': (
            (
                {
                    'Обществознание (Б)': models.MatInf.objects.filter(d1=True),
                    'География (Б)': models.MatInf.objects.filter(d2=True),
                    'МХК (Б)': models.MatInf.objects.filter(d3=True),
                    'Теория познания (Б)': models.MatInf.objects.filter(d4=True),
                    'Биология (Б)': models.MatInf.objects.filter(d5=True),
                    'Физика (Б)': models.MatInf.objects.filter(d6=True),
                    'Химия (Б)': models.MatInf.objects.filter(d7=True),
                },
                {
                    'Решение сложных задач по математике': 1,
                    'Математические основы информатики': 1,
                    'Избранные главы учебников естественных наук': models.MatInf.objects.filter(d8=True),
                }
            ),
            models.MatInf.objects.all()
        ),
        'ФМ': (
            (
                {
                    'Обществознание (Б)': models.FizMat.objects.filter(d1=True),
                    'География (Б)': models.FizMat.objects.filter(d2=True),
                    'МХК (Б)': models.FizMat.objects.filter(d3=True),
                    'Теория познания (Б)': models.FizMat.objects.filter(d4=True),
                    'Биология (Б)': models.FizMat.objects.filter(d5=True),
                    'Химия (Б)': models.FizMat.objects.filter(d6=True),
                },
                {
                    'Решение сложных задач по математике': 1,
                    'Физические задачи повышенной сложности': 1,
                    'Астрономия': models.FizMat.objects.filter(d7=True),
                    'Избранные главы учебников естественных наук': models.FizMat.objects.filter(d8=True),
                }
            ),
            models.FizMat.objects.all()
        ),
        'ФТ': (
            (
                {
                    'Обществознание (Б)': models.FizTech.objects.filter(d1=True),
                    'География (Б)': models.FizTech.objects.filter(d2=True),
                    'МХК (Б)': models.FizTech.objects.filter(d3=True),
                    'Теория познания (Б)': models.FizTech.objects.filter(d4=True),
                    'Биология (Б)': models.FizTech.objects.filter(d5=True),
                    'Химия (Б)': models.FizTech.objects.filter(d6=True),
                },
                {
                    'Решение сложных задач по математике': 1,
                    'Инженерная графика (геометрическое и проекционное черчение)': models.FizTech.objects.filter(d7=True),
                    'Физические задачи повышенной сложности': 1,
                    'Астрономия': models.FizTech.objects.filter(d8=True),
                    'Избранные главы учебников естественных наук': models.FizTech.objects.filter(d9=True),
                }
            ),
            models.FizTech.objects.all()
        ),
        'ХИМ': (
            (
                {
                    'Обществознание (Б)': models.Him.objects.filter(d1=True),
                    'География (Б)': models.Him.objects.filter(d2=True),
                    'МХК (Б)': models.Him.objects.filter(d3=True),
                    'Теория познания (Б)': models.Him.objects.filter(d4=True),
                    'Информатика (Б)': models.Him.objects.filter(d5=True),
                    'Биология (Б)': models.Him.objects.filter(d6=True),
                },
                {
                    'Решение сложных задач по математике': models.Him.objects.filter(d7=True),
                    'Физические задачи повышенной сложности': models.Him.objects.filter(d8=True),
                    'Биологические задачи': models.Him.objects.filter(d9=True),
                    'Химические задачи повышенной сложности': 1,
                    'Химический практикум': models.Him.objects.filter(d10=True),
                    'Астрономия': models.Him.objects.filter(d11=True),
                }
            ),
            models.Him.objects.all()
        ),
        'БИО': (
            (
                {
                    'Обществознание (Б)': models.Bio.objects.filter(d1=True),
                    'География (Б)': models.Bio.objects.filter(d2=True),
                    'МХК (Б)': models.Bio.objects.filter(d3=True),
                    'Теория познания (Б)': models.Bio.objects.filter(d4=True),
                    'Информатика (Б)': models.Bio.objects.filter(d5=True),
                    'Физика (Б)': models.Bio.objects.filter(d6=True),
                },
                {
                    'Решение сложных задач по математике': models.Bio.objects.filter(d7=True),
                    'Информатика в задачах': models.Bio.objects.filter(d8=True),
                    'Биологические задачи повышенной сложности': 1,
                    'Сложные вопросы ботаники, зоологии, анатомии': models.Bio.objects.filter(d9=True),
                    'Химические задачи повышенной сложности': models.Bio.objects.filter(d10=True),
                    'Биологический практикум': models.Bio.objects.filter(d11=True),
                }
            ),
            models.Bio.objects.all()
        )
    }