job= Job(title = "js + react")
job.save()
job.skills.add(Skill.objects.all()[1],Skill.objects.all()[2])
job.save()