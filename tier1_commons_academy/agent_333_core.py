# agent_333_core.py
# Open Source CyberBios OS - Tier 1 & Tier 2 Execution Core
import sys
import traceback
from typing import Dict, Any

class CyberBiosAgent333:
    def __init__(self, model_version: str = "v2026.8-LLM"):
        self.model_version = model_version
        self.agent_id = "CyberBios Agent 333"

    def process_telemetry(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        """
        Processes telemetry data originating from Cyber Πέτρα and Cyber Πλέγμα nodes.
        Executes data-backed reasoning and safety cut validation.
        """
        try:
            device_id = payload.get("device_id")
            sector = payload.get("sector", "Community")
            watts = float(payload.get("watts", 0.0))

            if not device_id:
                raise ValueError("Payload missing critical identifier (device_id).")

            kwh_daily = round((watts * 24) / 1000, 2)

            if watts > 2000.0:
                status = "HIGH_CONSUMPTION_ALERT"
                recommendation = (
                    f"[{self.agent_id} | {sector}]: Καταγραφή {watts}W ({kwh_daily} kWh/day). "
                    f"Ενεργοποίηση πρωτοκόλλου εξοικονόμησης & αποσύνδεση φορτίων αιχμής."
                )
            else:
                status = "NORMAL_OPERATION"
                recommendation = f"[{self.agent_id} | {sector}]: Ομαλή κατανάλωση {watts}W."

            return {
                "status": status,
                "device_id": device_id,
                "sector": sector,
                "agent_response": recommendation,
                "pythagorean_academy_certified": True
            }

        except Exception as e:
            error_trace = traceback.format_exc()
            sys.stderr.write(f"[CYBERBIOS AGENT CRITICAL ERROR]:\n{error_trace}\n")
            return {"status": "ERROR", "traceback": error_trace}

if __name__ == "__main__":
    agent = CyberBiosAgent333()
    sample = {"device_id": "CYBER_PETRA_PROTO_01", "sector": "Retail Group", "watts": 2850.0}
    res = agent.process_telemetry(sample)
    print(res.get("agent_response"))
