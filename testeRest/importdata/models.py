from django.db import models

class IGDBGame(models.Model):

	id = models.IntegerField(
		('IGDB ID'),
		help_text=("Id do jogo na IGDB"),
		primary_key=True,
	)

	name = models.CharField(
		('name'),
		help_text=("Nome do Jogo"),
		max_length=100,
	)

	hypes = models.IntegerField(
		('Hypes'),
		help_text=("Number of access in the game befores its release"),
	)

	def __str__(self):
	    """
	    Returns the object as a string, the attribute that will represent
	    the object.
	    """

	    return self.name

	class Meta:
	    """
	    Some information about feedback class.
	    """
	    verbose_name = ("IGDB Game")
	    verbose_name_plural = ("IGDB Games")