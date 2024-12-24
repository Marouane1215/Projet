from django.shortcuts import render

def display_setup_time_view(request):
    # Récupérer les temps de réglage depuis la session
    setup_time = request.session.get('setup_time', None)

    if not setup_time:
        # Si les temps de réglage ne sont pas définis, afficher un message
        context = {
            'error': "Aucun temps de réglage enregistré. Veuillez les configurer d'abord."
        }
        return render(request, 'page/display_setup_time.html', context)

    # Fonction pour convertir les minutes en heures
    def convert_minutes_to_hours(minutes):
        hours = minutes // 60
        remainder_minutes = minutes % 60
        return f"{hours}h {remainder_minutes}min"

    # Préparer les données converties pour l'affichage
    converted_setup_time = {
        machine: {job: convert_minutes_to_hours(time) for job, time in jobs.items()}
        for machine, jobs in setup_time.items()
    }

    num_machines = len(converted_setup_time)
    jobs_list = list(next(iter(converted_setup_time.values())).keys())  # Récupérer les jobs à partir de la première machine

    context = {
        'setup_time': converted_setup_time,  # Données converties
        'num_machines': num_machines,
        'jobs_list': jobs_list,
    }
    return render(request, 'page/c.html', context)
