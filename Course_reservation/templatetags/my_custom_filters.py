from django import template

register = template.Library()

@register.filter(name='week')
def week(v1):
    v1 = v1.weekday()+1
    chinese_numbers = {
        1: '星期一',
        2: '星期二',
        3: '星期三',
        4: '星期四',
        5: '星期五',
        6: '星期六',
        7: '星期七',
    }
    return chinese_numbers[v1]

@register.filter(name='divisibleby')
def divisibleby(v1):
    v1=v1%5

    return v1
