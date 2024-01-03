#image bg RayitasRoom = "Room.jpg" 
image bg RayitasRoom = "/Background/Room.jpg" 
image mochila = "mochila.png"
image mesa = "mesa.png"  


label start:

    #scene RayitasRoom
    scene bg RayitasRoom with Fade(0.5, 4.5, 0.5):  
        align(0.5, 0.5) zoom 1.9 
        matrixcolor TintMatrix("#071b54")
    "" 
    play sound "Alarma.mp3"
    menu:     
        "Apagar la alarma (5 min más)":
            stop sound
            show bg RayitasRoom with Fade(0.5, 1.0, 0.5)
            "Oh maldición, no puedo llegar tarde de nuevo! {p=1}
            Debo preparar mis libros cuanto antes{p=0}
            si no quiero quedar fuera."
            show bg RayitasRoom:
                matrixcolor TintMatrix("#ffffff")
            call Minujuego_Mochila

        "Levantarse":
            show bg RayitasRoom
            "Debería prepararme cuanto antes para la escuela,{p=0}
            Primero mis cosas y luego desayuno antes de ir."
            stop sound
            show bg RayitasRoom:
                matrixcolor TintMatrix("#ffffff")
            call Minujuego_Mochila    
    jump almuerzo   
         
label Minujuego_Mochila:
    play music "Hurry.mp3"
    show mochila:
        zoom 1.3, xpos 10, ypos 500#, matrixcolor TintMatrix("#adf542")
    ""
    stop music
    return

#CodeBy: RamaHD_