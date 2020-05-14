from Section22_TemplateMethod.Practice.AbstractCardGame import AbstractCardGame


class PermanentDamageAbstractCardGame(AbstractCardGame):
    def hit(self, attacker, defender):
        defender.health -= attacker.attack
