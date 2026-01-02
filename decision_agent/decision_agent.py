class DecisionAgent:
    def decide(self, urgency, customer_type, severity_score):
        # Normalize inputs (CRITICAL)
        urgency = str(urgency).upper()
        customer_type = str(customer_type).lower()

        if urgency == "HIGH" and customer_type == "premium":
            return "ESCALATE_TO_HUMAN"

        if severity_score <= 3:
            return "AUTO_RESOLVE"

        if urgency == "UNKNOWN":
            return "MANUAL_REVIEW"

        return "ROUTE_TO_OPERATIONS"
