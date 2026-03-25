voici une « check‑list » simple pour éviter ce genre de problèmes :

Toujours suivre le même schéma pour une nouvelle ressource (Student, Employee, Blog, etc.)

Modèle dans models.py
makemigrations + migrate
Serializer dans serializers.py
Vue DRF dans views.py
Routes dans urls.py (/api/v1/.../)
Nommer pareil partout

Si tu écris path('', views.employees) dans urls.py, vérifie qu’il y a bien une fonction ou classe employees dans views.py.
Même chose pour Blogs, BlogDetail, etc.
Bien séparer “site web” et “API”

URLs “HTML” (templates, HttpResponse) : dans students.urls, employees.urls, blogs.urls incluses directement sans /api/v1/.
URLs API (JSON, DRF) : uniquement dans urls.py, incluses une seule fois avec path('api/v1/', include('api.urls')).
Après chaque ajout/modif importante : tester une par une

Lancer le serveur.
Tester l’URL dans le navigateur ou Postman (/api/v1/students/, /api/v1/employees/, /api/v1/blogs/…), vérifier le code retour.
Lire le message d’erreur jusqu’au bout

AttributeError: module ... has no attribute ... → mauvais nom de vue ou vue manquante.
404 Not Found → l’URL n’existe pas dans tes urlpatterns (ou mauvais chemin).
Ne pas dupliquer les mêmes routes partout

Évite d’inclure deux fois les mêmes urls sur des chemins différents si tu n’en as pas besoin, ça complique le debug.
Si tu veux, on peut prendre un exemple concret (par ex. “je veux ajouter une ressource Comments”) et je te montre toutes les étapes une par une, que tu pourras réutiliser à chaque fois.