import gif_pygame
import pygame
from random import *
from settings import *

from .VentanaView import VentanaView


class CanchaView(VentanaView):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        self.__renderizaciones = {}
        self.__estadio = camp_nou
        self.__estadio_cancha = barcelona

    def mostrar(self):
        self._botones = {}
        pygame.display.set_caption("GAMEPLAY")
        self._pantalla.fill(NEGRO)
        # self._pantalla.blit(marcador, (int(ANCHO * 0.76), int(ALTO * 0.01)))
        # self._pantalla.blit(marcador, (int(ANCHO * 0.2), int(ALTO * 0.55)))
        estadio = self.__estadio_cancha
        self._pantalla.blit(estadio, (int(ANCHO * 0.01), int(ALTO * 0.01)))
        self.mostrar_jugadores()
        TIEMPO = get_fuente(50).render("TIEMPO", True, BLANCO)
        self._pantalla.blit(TIEMPO, (int(ANCHO * 0.84), int(ALTO * 0.05)))
        ATAJADA_GIF.render(self._pantalla, (int(ANCHO * 0.25), int(ALTO * 0.05)))
        ATAJADA_GIF.pause()

        PASE = self._mostrar_boton(
            boton_negro2,
            (ANCHO * 0.1, ALTO * 0.65),
            "PASE",
            get_fuente(50),
            BLANCO,
            "Green",
        )

        TIRO = self._mostrar_boton(
            boton_negro2,
            (ANCHO * 0.1, ALTO * 0.75),
            "TIRO",
            get_fuente(50),
            BLANCO,
            "Green",
        )

        GAMBETA = self._mostrar_boton(
            boton_negro2,
            (ANCHO * 0.1, ALTO * 0.85),
            "GAMBETA",
            get_fuente(50),
            BLANCO,
            "Green",
        )

        INTERCEPTAR = self._mostrar_boton(
            boton_negro2,
            (ANCHO * 0.1, ALTO * 0.95),
            "INTERCEPTAR",
            get_fuente(50),
            BLANCO,
            "Green",
        )

        self._botones["interceptar"] = INTERCEPTAR
        self._botones["gambeta"] = GAMBETA
        self._botones["tiro"] = TIRO
        self._botones["pase"] = PASE

    def mostrar_mensaje(self, mensaje, y):
        fuente = get_fuente(75)
        texto_render = fuente.render(mensaje, True, "White")
        self._pantalla.blit(
            texto_render, (ANCHO / 2 - texto_render.get_width() / 2, y + 300)
        )
        pygame.display.flip()

    def set_estadio(self, estadio):
        self.__estadio = estadio

    def setear_estadio_cancha(self):
        if self.__estadio == camp_nou:
            self.__estadio_cancha = barcelona
        elif self.__estadio == bernabeu:
            self.__estadio_cancha = madrid
        elif self.__estadio == old_traford:
            self.__estadio_cancha = manchester
        elif self.__estadio == monumental:
            self.__estadio_cancha = nuñez
        elif self.__estadio == bombonera:
            self.__estadio_cancha = boca
        elif self.__estadio == azteca:
            self.__estadio_cancha = mexico
        elif self.__estadio == malasia:
            self.__estadio_cancha = malasya
    def mostrar_jugadores(self):
        jug_us= pygame.image.load(EQUIPO_US)
        jug_chica=pygame.transform.scale(jug_us,(10,10))
        jug_cpu= pygame.image.load(EQUIPO_CPU)
        jug_cpu_chica=pygame.transform.scale(jug_cpu,(10,10))
        lista=[("4-3-3"),("4-4-2")]
        lis = choice(lista) #esto lo hice por el simple echo si cambiaba la formacion, pero hay que sacarlo por que se ejecuta las dos formaciones rapidamente xd
        #HAY QUE ARREGLAR DE DONDE IRA ESTA IMPRESION, POR QUE NO SE COMO IMPLEMENTARLO EN EL MINIMAPA
        for posicion in POSICIONES:
            coordenadas= FORMACION_USUARIO[lis][posicion]
            for coordenada in coordenadas:
                x= coordenada[0]
                y= coordenada[1]
                self._pantalla.blit(jug_chica,(x,y))
                self.cambiar_color_jugador(x,y)
            coordenadas = FORMACION_CPU[lis][posicion]
            for coordenada in coordenadas:
                x = coordenada[0]
                y = coordenada[1]
                self._pantalla.blit(jug_cpu_chica, (x, y))
                self.cambiar_color_jugador(x,y)
    def cambiar_color_jugador(self,x,y):
        # Implementación de la función aquí
        con_pelota= pygame.image.load(JUG_CONPELOTA)
        jug_conpelota=pygame.transform.scale(con_pelota,(10,10))
        for posicion in POSICIONES:
            coordenadas = FORMACION_USUARIO["4-3-3"][posicion]
            for coordenada in coordenadas:
                if coordenada == (x, y):
                    # Cambiar el color del jugador
                    if posicion == "jugador_del_usuario":
                        # Cambiar de rojo a negro
                        self._pantalla.blit(jug_conpelota, (x, y))
                    elif posicion == "jugador_del_cpu":
                        # Cambiar de azul a negro
                        self._pantalla.blit(jug_conpelota, (x, y))