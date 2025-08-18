from dispatch.fourmi_dispatcher import assigner_fourmi, liberer_fourmi, afficher_statut

afficher_statut()
id = assigner_fourmi("transfert", "Berserk")
afficher_statut()
liberer_fourmi(id)
afficher_statut()