import turtle
x=turtle.Turtle()
def rectangle(width,hight,color):
    """trace un rectangle de longueur 'width' et de largeur 'hight' et de couleur 'color'
        pre: `color` spécifie une couleur.
        La tortue `x` est initialisée.
        La tortue est placée à un sommet et orientée en direction d'un côté du rectangle.
        post: Le rectangle a été tracé sur la droite du premier côté.
        La tortue est à la même position et orientation qu'au départ.
        """
    x.color(color)
    x.pendown()
    x.begin_fill()
    for i in range(2):
        x.forward(width)
        x.left(90)
        x.forward(hight)
        x.left(90)
    x.penup()
    x.end_fill()