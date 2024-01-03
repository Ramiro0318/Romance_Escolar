image bg scene2 = "images/Background/Cocina.jpg"

define e = Character("Elizabeth")
image Elizabeth normal = "/Characters/Elizabeth/Elizabeth_Normal.png"
image Elizabeth alegre = "/Characters/Elizabeth/Elizabeth_Alegre.png"
image Elizabeth enojada = "/Characters/Elizabeth/Elizabeth_Enojada.png"
image Elizabeth guino = "/Characters/Elizabeth/Elizabeth_Guiño.png"
image Elizabeth seria = "/Characters/Elizabeth/Elizabeth_Seria.png"


label almuerzo:
    scene bg scene2 with Fade(0.5, 0.0, 0.5):
        align (0.5, 0.5) zoom 0.5
    "Hola"
    show Elizabeth normal with Dissolve(0.5)
    e "¡Hola hermanito! Veo que te levantaste temprano hoy, 
    a veces puedes ser un poco responsable."
    "— No es como si despertara tarde tan seguido, solo ha 
    ocurrido un par de veces"
    show Elizabeth alegre

    e "Y aún así estás a un solo retardo de ser suspendido\n {i}*Jeje*{/i}"
    "— No pasas nada por alto, hermana\n *Suspiro*"
    show Elizabeth enojada with dissolve
    #play sound "Clin.mp3"
    #Animacion

    menu:
        "Es mi trabajo cómo hermana mayor cuidar de mi pequeño 
        hermano, ten más cuidado, ¿si?"
        "...":
            show Elizabeth guino with dissolve
            e"Oh vamos, no tienes que ponerte tan serio al respecto."
            show Elizabeth seria with dissolve
            e"Cómo sea es tarde y tenemos que irnos a la escuela ya mismo."
            "(Definitivamente le disgusta que no le siga el juego)"
            

        "¡Para, me ruborizas!":
            show Elizabeth alegre with dissolve
            e"¡jajaja, Eres tan adorable cuando te pones así!"
            "(Pues yo no le veo la gracia){p}
            ¿Podrías al menos no tratarme así en público?{p=0.5} 
            La gente pensará cosas."
            show Elizabeth normal #transicion a enojada
            e"¿Y eso que tiene de malo?{w=1} ¿Tienes a alguna chica?"
            "(A veces puede ser muy infantil, {p=0.5}bueno, se nos hace tarde
            así que debemos irnos)"
    hide Elizabeth 
    show bg scene2 with Fade(0.5, 20.0, 0.5)
    ""
    return
            
        




