class PolicyIndConfig:
    """
    指标转换策略
    True 入  False 出
    """

    def er(self, *lines):
        lines = lines[0]
        if min(lines[0], lines[1]) > 0:
            return True
        elif max(lines[0], lines[1]) < 0:
            return False

    def po(self, *lines):
        lines = lines[0]

        if lines[0] > 0:
            return True
        else:
            return False

    def dpo(self, *lines):
        lines = lines[0]

        if lines[0] > 0:
            return True
        else:
            return False

    def pac(self, *lines):
        lines = lines[0]

        if lines[2] > lines[1]:
            return True
        elif lines[2] < lines[0]:
            return False

    def maamt(self, *lines):
        lines = lines[0]

        if lines[0] > 0:
            return True
        else:
            return False

    def madisplaced(self, *lines):
        lines = lines[0]

        if lines[0] > 0:
            return True
        else:
            return False


# 指标对应关系  self.p.er_period_me1 = self.ind_params.get("ER")[0]
ind_name_relation = {
    "dpo_period": "DPO_0",
    "er_period_me1": "ER_0",
    "maamt_period_me1": "MAAMT_0",
    "madisp_period_signal": "MADisplaced_1",
    "madisp_period_me1": "MADisplaced_0",
    "pac_period_low": "PAC_0",
    "pac_period_high": "PAC_1",
    "po_period_short": "PO_0",
    "po_period_long": "PO_1"
}
