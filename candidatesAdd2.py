candidate1= Candidate(name = "Yonata Agever",title = "Works at intel")
candidate1.save()
candidate1.skills.add(Skill.objects.all()[1],Skill.objects.all()[2])
candidate1.save()