import sys

import pygame

from model.logic.Dificultades import *
from model.logic.EquipoLogico import EquipoLogico
from model.logic.formacion import *
from model.logic.Partido import Partido
from settings import *
from view.JugarView import JugarView

from .CanchaViewControlador import CanchaController
from .Controlador import Controlador
from controller.LoginJugarViewControlador import LoginJugarViewControlador


class JugarController(Controlador):
    def __init__(self):
        super().__init__()
        self.__genero_equipo = EquipoLogico("Equipo FC")
        self._view = JugarView(SCREEN, str(self.__genero_equipo.get_nombre()))
        self.__formacion_actual = FORMACION_PREDETERMINADA
        self.__comienza_partida = False
        self.__dado_apretado = False
        self.__cancha = CanchaController(SCREEN, Facil(), self.__genero_equipo)
        self.__LoginEquipo = LoginJugarViewControlador(SCREEN)

    def manejar_eventos(self, eventos, mouse_pos):
        botones = self._view.get_botones()
        from controller.MenuViewControlador import MenuController

        for event in eventos:
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if botones["dado"].checkForInput(mouse_pos):  # Boton del Dado
                    self.__dado_apretado = True
                    self.__genero_equipo.nuevo_equipo()
                    self._view.renderizar(self.__genero_equipo._jugadores)
                    self.__comienza_partida = True
                elif botones["comienza"].checkForInput(
                    mouse_pos
                ):  # Boton Comenzar Partia
                    if self.__comienza_partida:
                        self._view.ocultar_visibilidad()
                        self.__cancha.main_loop()
                elif botones["atras"].checkForInput(mouse_pos):  # Boton Back
                    self._view.ocultar_visibilidad()
                    menu_principal = MenuController()
                    menu_principal.main_loop()
                elif botones["cambiar_formacion_atras"].checkForInput(
                    mouse_pos
                ) or botones["cambiar_formacion_adelante"].checkForInput(
                    mouse_pos
                ):  # flechas para cambiar formacion
                    if self.__formacion_actual == "4-4-2":
                        self.__formacion_actual = "4-3-3"
                        self.__genero_equipo.set_formacion(Formacion433())
                    else:
                        self.__formacion_actual = "4-4-2"
                        self.__genero_equipo.set_formacion(Formacion442())
                    self._view.texto_formacion(self.__formacion_actual)
                elif botones["cambiar_estadio_adelante"].checkForInput(mouse_pos):
                    self.__cambiar_estadio("Adelante")
                elif botones["cambiar_estadio_atras"].checkForInput(mouse_pos):
                    self.__cambiar_estadio("Atras")
                elif botones["usuario"].checkForInput(mouse_pos):
                    self.__LoginEquipo.main_loop()

            clock.tick(FPS)
            pygame.display.update()

    def main_loop(self):
        while True:
            mouse_pos = pygame.mouse.get_pos()
            self._view.mostrar()  # Mostrar el menú
            self._view.dibujar_formaciones(
                self._view._pantalla,
                FORMACIONES,
                self.__formacion_actual,
                self.__genero_equipo._jugadores,
                self.__dado_apretado,
            )
            self._view.texto_formacion(self.__formacion_actual)
            eventos = pygame.event.get()  # Manejar eventos
            self.manejar_eventos(eventos, mouse_pos)
            clock.tick(60)
            pygame.display.update()

    def __cambiar_estadio(self, donde):
        estadios = [
            camp_nou,
            monumental,
            bernabeu,
            bombonera,
            azteca,
            malasia,
            old_traford,
        ]
        estadio_actual = self._view.get_estadio()
        indice_actual = estadios.index(estadio_actual)
        if donde == "Adelante":
            nuevo_indice = (indice_actual + 1) % len(estadios)
        else:
            nuevo_indice = (indice_actual - 1) % len(estadios)
        self._view.cambiar_estadio(estadios[nuevo_indice])
