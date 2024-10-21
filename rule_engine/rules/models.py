from django.db import models

class Rule(models.Model):
    rule_string = models.TextField()  # Original rule string
    ast = models.JSONField()  # Store AST as JSON
    created_at = models.DateTimeField(auto_now_add=True)
