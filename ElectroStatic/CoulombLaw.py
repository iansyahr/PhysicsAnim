#SEMI FINAL

from manim import *
config.background_color = '#ece6e2'

class Partikel(Scene):
  def construct(self):
    
    #Make Particle
    p1 = Circle()
    p1.set_fill('#2c83db',opacity = 1) #blue color
    p1.set_stroke(color=BLACK, width=1)

    p2 = Circle()
    p2.set_fill('#db462c',opacity = 1) # red color
    p2.set_stroke(color=BLACK, width=1)

    #Position p1 and p2
    p1.shift(LEFT*3)
    p2.shift(RIGHT*3)
    
    #Grouping p1 and p2 to pgrup
    pgrup = VGroup(p1,p2)

    #distance arrow
    panah = DoubleArrow(p1,p2,width = 2,color = BLACK)

    #LaTex
    p1text = MathTex("q_1",color = BLACK).scale(1.5)
    p2text = MathTex("q_2",color = BLACK).scale(1.5)
    jaraktext = MathTex("r",color = BLACK).scale(1.5)
    coulomb = MathTex("F = k ","{q_1","q_2" ,"\\over" ,"r^2}",color = BLACK).scale(1.5)
    coulomb.shift(DOWN*1.5)
    textgrup = VGroup(p1text,p2text,jaraktext)
    fadegrup = VGroup(textgrup,pgrup,panah)
    fadegrup1 = VGroup(fadegrup,coulomb)

    #Animate
    self.play(FadeInFrom(pgrup,direction = DOWN),run_time = 1)
    self.play(Write(p1text.next_to(p1,DOWN)))
    self.play(Write(p2text.next_to(p2,DOWN)))
    self.play(GrowFromCenter(panah))
    self.play(Write(jaraktext.next_to(panah,DOWN)))
    self.wait()
    self.play(fadegrup.animate.shift(UP*1.5))
    self.play(ReplacementTransform(p1text[0].copy(),coulomb[1]),
              ReplacementTransform(p2text[0].copy(),coulomb[2]),
              ReplacementTransform(jaraktext[0].copy(),coulomb[4]),
              Write(coulomb[0]),
              Write(coulomb[3]))
    self.wait(1)
    self.play(FadeToColor(p1,'#db462c'),FadeToColor(p2,'#2c83db'))
    self.wait(3)
    self.play(FadeOutAndShift(fadegrup1, direction = UP))
