from Section22_TemplateMethod.Practice.AbstractCardGame import AbstractCardGame


class TemporaryDamageAbstractCardGame(AbstractCardGame):
    def hit(self, attacker, defender):
        old_health = defender.health
        defender.health -= attacker.attack
        if defender.health > 0:
            defender.health = old_health
