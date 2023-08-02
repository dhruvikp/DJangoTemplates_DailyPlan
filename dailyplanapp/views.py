from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

daily_plans = {
    "monday": "Eat one Apple",
    "tuesday": "Eat one Avacado",
    "wednesday": "Eat one Orange",
    "thursday": "Its a vagitable day, Eat vegitables",
    "friday": "Drink Junice",
    "saturday": "Eat Banana",
    "sunday": None
}

# Create your views here.
def index(request):
    # resp_content = render_to_string("dailyplanapp/plans.html")
    # return HttpResponse(resp_content)
    days = list(daily_plans.keys())
    return render(request, "dailyplanapp/plans.html", {"days": days})


def daily_diet_by_number(request, day):
    days = list(daily_plans.keys())
    print(days)

    if(day > len(days)) :
        return HttpResponseNotFound("Invalid month")
        
    redirect_day = days[day-1]
    redirect_path = reverse("daily-diet", args=[redirect_day])
    return HttpResponseRedirect(redirect_path)


def daily_diet(request, day):
    try:
        current_day_plan = daily_plans[day]
    except:
        return HttpResponseNotFound("This day is not supported!")
    # return HttpResponse(current_day_plan)
    data = {
        "day": day,
        "plan": current_day_plan
    }
    return render(request, "dailyplanapp/dailyplan.html", data)