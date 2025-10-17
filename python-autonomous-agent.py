"""
Autonomous Task Planning AI Agent
Author: Aadarsh Potadar

A versatile AI agent that autonomously plans and executes tasks by:
1. Analyzing environmental conditions
2. Checking resource availability
3. Calculating requirements
4. Making intelligent decisions
5. Planning optimal execution paths

UNIVERSAL APPLICATIONS:
- Drones: Mission planning (FlytBase, DJI, etc.)
- Logistics: Delivery route optimization (Amazon, FedEx)
- Manufacturing: Production scheduling (Tesla, factories)
- Healthcare: Patient scheduling (hospitals)
- Energy: Grid management (power companies)

This demonstrates core agentic AI: autonomous decision-making,
tool usage, multi-step reasoning, and error handling.
"""

import json
import random
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from enum import Enum

class TaskType(Enum):
    """Different task types for various industries"""
    DRONE_MISSION = "drone_mission"
    DELIVERY_ROUTE = "delivery_route"
    PRODUCTION_JOB = "production_job"
    MAINTENANCE_CHECK = "maintenance_check"
    INSPECTION_TASK = "inspection_task"

class ResourceAPI:
    """Simulates resource availability API (universal for any industry)"""
    
    @staticmethod
    def get_available_resources(resource_type: str) -> List[Dict]:
        """
        Get available resources (drones, vehicles, machines, etc.)
        
        Works for:
        - Drones (FlytBase, DJI)
        - Delivery vehicles (Amazon, FedEx)
        - Manufacturing robots (Tesla, factories)
        - Medical equipment (hospitals)
        """
        if resource_type == "drone":
            resources = [
                {"id": "RESOURCE-001", "capacity": 95, "status": "available", "location": "Base-A"},
                {"id": "RESOURCE-002", "capacity": 45, "status": "available", "location": "Base-A"},
                {"id": "RESOURCE-003", "capacity": 85, "status": "charging", "location": "Base-B"},
                {"id": "RESOURCE-004", "capacity": 100, "status": "available", "location": "Base-A"},
            ]
        elif resource_type == "vehicle":
            resources = [
                {"id": "VEHICLE-001", "capacity": 80, "status": "available", "location": "Warehouse-1"},
                {"id": "VEHICLE-002", "capacity": 60, "status": "available", "location": "Warehouse-2"},
                {"id": "VEHICLE-003", "capacity": 90, "status": "available", "location": "Warehouse-1"},
            ]
        else:
            resources = [
                {"id": "UNIT-001", "capacity": 75, "status": "available", "location": "Station-A"},
                {"id": "UNIT-002", "capacity": 95, "status": "available", "location": "Station-B"},
            ]
        
        return resources

class EnvironmentAPI:
    """Simulates environment/condition checking API"""
    
    @staticmethod
    def check_conditions(location: str, task_type: str) -> Dict:
        """
        Universal condition checker
        
        For drones: Weather conditions
        For logistics: Traffic conditions
        For manufacturing: Equipment status
        For healthcare: Facility availability
        """
        conditions_map = {
            "drone_mission": {
                "type": "weather",
                "safe": random.choice([True, True, True, False]),  # 75% safe
                "details": {
                    "condition": random.choice(["Clear", "Cloudy", "Windy"]),
                    "wind_speed": random.randint(5, 35),
                    "visibility": random.randint(5, 15)
                }
            },
            "delivery_route": {
                "type": "traffic",
                "safe": random.choice([True, True, False]),  # 66% safe
                "details": {
                    "traffic_level": random.choice(["Low", "Moderate", "Heavy"]),
                    "estimated_delay_min": random.randint(0, 45),
                    "road_status": random.choice(["Clear", "Construction"])
                }
            },
            "production_job": {
                "type": "facility",
                "safe": True,
                "details": {
                    "machine_status": "Operational",
                    "temperature": random.randint(20, 25),
                    "power_status": "Stable"
                }
            }
        }
        
        return conditions_map.get(task_type, conditions_map["drone_mission"])

class UniversalPlanningAgent:
    """
    Universal AI Agent for Task Planning
    
    Can be applied to:
    - Autonomous Drones (FlytBase, DJI, Skydio)
    - Logistics & Delivery (Amazon, FedEx, UPS)
    - Manufacturing (Tesla, factories, robotics)
    - Healthcare (scheduling, resource allocation)
    - Energy Management (grid optimization)
    - Warehouse Automation (inventory, picking)
    """
    
    def __init__(self, industry: str = "autonomous_systems"):
        self.industry = industry
        self.resource_api = ResourceAPI()
        self.environment_api = EnvironmentAPI()
        self.decision_log = []
        
    def log_decision(self, step: str, decision: str, reasoning: str):
        """Log agent's decision-making process (universal)"""
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "step": step,
            "decision": decision,
            "reasoning": reasoning
        }
        self.decision_log.append(entry)
        print(f"\n[AGENT DECISION] {step}")
        print(f"Decision: {decision}")
        print(f"Reasoning: {reasoning}")
        print("-" * 70)
    
    def check_environment_safety(self, location: str, task_type: str) -> tuple[bool, str]:
        """
        Tool 1: Environment/Condition Check (Universal)
        
        Adapts to context:
        - Drones → Weather
        - Logistics → Traffic
        - Manufacturing → Equipment status
        - Healthcare → Facility availability
        """
        print(f"\n[TOOL CALL] Checking conditions for {location}...")
        conditions = self.environment_api.check_conditions(location, task_type)
        
        print(f"Condition Type: {conditions['type']}")
        print(f"Details: {json.dumps(conditions['details'], indent=2)}")
        
        if not conditions['safe']:
            if conditions['type'] == 'weather':
                return False, f"Unsafe weather: Wind {conditions['details']['wind_speed']} km/h"
            elif conditions['type'] == 'traffic':
                return False, f"Heavy traffic: {conditions['details']['estimated_delay_min']} min delay"
            else:
                return False, f"Conditions not favorable: {conditions['details']}"
        
        return True, f"Conditions favorable for task execution"
    
    def select_optimal_resource(self, resource_type: str, min_capacity: int = 70) -> Optional[Dict]:
        """
        Tool 2: Resource Selection (Universal)
        
        Selects:
        - Best drone (for aerial tasks)
        - Best vehicle (for delivery)
        - Best machine (for production)
        - Best equipment (for operations)
        """
        print(f"\n[TOOL CALL] Fetching available {resource_type}s...")
        resources = self.resource_api.get_available_resources(resource_type)
        
        print(f"Total {resource_type}s in fleet: {len(resources)}")
        
        # Filter available resources
        available = [r for r in resources if r["status"] == "available" and r["capacity"] >= min_capacity]
        
        if not available:
            self.log_decision(
                "Resource Selection",
                "FAILED",
                f"No {resource_type} available with capacity >= {min_capacity}%"
            )
            return None
        
        # Select resource with highest capacity
        best_resource = max(available, key=lambda x: x["capacity"])
        
        self.log_decision(
            "Resource Selection",
            f"Selected {best_resource['id']}",
            f"Capacity: {best_resource['capacity']}%, Status: {best_resource['status']}"
        )
        
        return best_resource
    
    def calculate_resource_requirement(self, 
                                      distance: float = 0, 
                                      complexity: str = "medium",
                                      duration: int = 0) -> int:
        """
        Tool 3: Requirement Calculation (Universal)
        
        Calculates:
        - Battery % (for drones)
        - Fuel/Energy (for vehicles)
        - Machine time (for production)
        - Staff hours (for services)
        """
        print(f"\n[TOOL CALL] Calculating resource requirements...")
        
        # Complexity multiplier
        complexity_map = {"low": 1.0, "medium": 1.3, "high": 1.6}
        multiplier = complexity_map.get(complexity, 1.3)
        
        # Base calculation (adaptable formula)
        if distance > 0:
            # Distance-based (logistics, drones)
            base_requirement = distance * 1.5
        elif duration > 0:
            # Time-based (services, production)
            base_requirement = duration * 0.8
        else:
            # Default
            base_requirement = 30
        
        # Apply complexity and safety margin
        total_required = base_requirement * multiplier * 1.2  # 20% safety
        
        print(f"Task complexity: {complexity}")
        print(f"Base requirement: {base_requirement:.1f}%")
        print(f"Safety margin included: 20%")
        print(f"Total required capacity: {total_required:.1f}%")
        
        return int(total_required)
    
    def plan_execution_path(self, task_details: Dict) -> Dict:
        """
        Tool 4: Execution Planning (Universal)
        
        Plans:
        - Flight path (drones)
        - Delivery route (logistics)
        - Production steps (manufacturing)
        - Task sequence (operations)
        """
        print(f"\n[TOOL CALL] Planning execution path...")
        
        start = task_details.get("start_location", "Base")
        end = task_details.get("end_location", "Target")
        
        # Generate execution steps
        num_steps = random.randint(3, 7)
        steps = []
        
        for i in range(num_steps):
            steps.append({
                "step": i + 1,
                "action": f"Execute phase {i + 1}",
                "estimated_time_min": random.randint(5, 20)
            })
        
        total_time = sum(step["estimated_time_min"] for step in steps)
        
        plan = {
            "start": start,
            "end": end,
            "total_steps": num_steps,
            "estimated_duration_min": total_time,
            "steps": steps,
            "contingency_plan": "Return to base if issues arise"
        }
        
        print(f"Execution path: {start} → {end}")
        print(f"Total steps: {num_steps}")
        print(f"Estimated duration: {total_time} minutes")
        
        return plan
    
    def make_autonomous_decision(self, task_request: Dict) -> Dict:
        """
        MAIN AGENTIC AI LOGIC
        
        Autonomous decision-making for ANY industry:
        1. Check environment/conditions
        2. Calculate requirements
        3. Select optimal resource
        4. Plan execution
        5. Make final decision
        """
        print("\n" + "="*70)
        print("UNIVERSAL AUTONOMOUS PLANNING AGENT")
        print(f"Industry: {self.industry.upper()}")
        print("="*70)
        print(f"\nTask Request Received:")
        print(json.dumps(task_request, indent=2))
        
        # Determine task type and resource type
        task_type = task_request.get("task_type", "drone_mission")
        resource_type = task_request.get("resource_type", "drone")
        
        # Step 1: Environment/Condition Check
        safe, reason = self.check_environment_safety(
            task_request.get("location", "Unknown"),
            task_type
        )
        
        if not safe:
            self.log_decision(
                "Environment Analysis",
                "TASK REJECTED",
                reason
            )
            return {
                "task_approved": False,
                "reason": reason,
                "decision_log": self.decision_log
            }
        
        self.log_decision(
            "Environment Analysis",
            "CONDITIONS APPROVED",
            reason
        )
        
        # Step 2: Calculate Requirements
        distance = task_request.get("distance", 0)
        complexity = task_request.get("complexity", "medium")
        duration = task_request.get("duration", 0)
        
        required_capacity = self.calculate_resource_requirement(distance, complexity, duration)
        
        self.log_decision(
            "Requirement Analysis",
            f"Required Capacity: {required_capacity}%",
            f"Distance: {distance}, Complexity: {complexity}"
        )
        
        # Step 3: Select Optimal Resource
        selected_resource = self.select_optimal_resource(resource_type, required_capacity)
        
        if not selected_resource:
            return {
                "task_approved": False,
                "reason": f"No {resource_type} available with required capacity ({required_capacity}%)",
                "decision_log": self.decision_log
            }
        
        # Step 4: Plan Execution
        execution_plan = self.plan_execution_path(task_request)
        
        # Step 5: Final Autonomous Decision
        self.log_decision(
            "Final Decision",
            "TASK APPROVED",
            f"All checks passed. {selected_resource['id']} ready for deployment."
        )
        
        # Return comprehensive plan
        return {
            "task_approved": True,
            "resource_assigned": selected_resource["id"],
            "resource_capacity": f"{selected_resource['capacity']}% (required: {required_capacity}%)",
            "execution_plan": execution_plan,
            "conditions_status": reason,
            "estimated_completion": f"{execution_plan['estimated_duration_min']} minutes",
            "decision_log": self.decision_log,
            "safety_checks": {
                "environment": "PASS",
                "resource_capacity": "PASS",
                "availability": "PASS"
            }
        }


def demo_multiple_industries():
    """
    Demonstrate agent working across different industries
    """
    print("\n" + "="*70)
    print("UNIVERSAL AI AGENT - MULTI-INDUSTRY DEMONSTRATION")
    print("="*70)
    
    # Example 1: Drone Operations (FlytBase)
    print("\n\n" + "="*70)
    print("USE CASE 1: AUTONOMOUS DRONE OPERATIONS (FlytBase, DJI, Skydio)")
    print("="*70)
    agent_drone = UniversalPlanningAgent("drone_operations")
    drone_task = {
        "task_type": "drone_mission",
        "resource_type": "drone",
        "location": "Solar Farm Alpha",
        "distance": 25,
        "complexity": "medium",
        "start_location": "Base-A",
        "end_location": "Solar Farm Alpha"
    }
    result1 = agent_drone.make_autonomous_decision(drone_task)
    print(f"\nRESULT: {'✓ APPROVED' if result1['task_approved'] else '✗ REJECTED'}")
    
    # Example 2: Logistics/Delivery
    print("\n\n" + "="*70)
    print("USE CASE 2: DELIVERY ROUTE PLANNING (Amazon, FedEx, DoorDash)")
    print("="*70)
    agent_logistics = UniversalPlanningAgent("logistics")
    delivery_task = {
        "task_type": "delivery_route",
        "resource_type": "vehicle",
        "location": "Downtown District",
        "distance": 15,
        "complexity": "high",
        "start_location": "Warehouse-1",
        "end_location": "Customer Location"
    }
    result2 = agent_logistics.make_autonomous_decision(delivery_task)
    print(f"\nRESULT: {'✓ APPROVED' if result2['task_approved'] else '✗ REJECTED'}")
    
    # Example 3: Manufacturing
    print("\n\n" + "="*70)
    print("USE CASE 3: PRODUCTION SCHEDULING (Tesla, Factories, Robotics)")
    print("="*70)
    agent_manufacturing = UniversalPlanningAgent("manufacturing")
    production_task = {
        "task_type": "production_job",
        "resource_type": "machine",
        "location": "Factory Floor A",
        "duration": 45,
        "complexity": "low",
        "start_location": "Station-A",
        "end_location": "Station-B"
    }
    result3 = agent_manufacturing.make_autonomous_decision(production_task)
    print(f"\nRESULT: {'✓ APPROVED' if result3['task_approved'] else '✗ REJECTED'}")
    
    # Summary
    print("\n\n" + "="*70)
    print("MULTI-INDUSTRY CAPABILITY DEMONSTRATED")
    print("="*70)
    print("\nThis single AI agent can autonomously plan tasks for:")
    print("✓ Drone Operations (FlytBase, DJI, Skydio)")
    print("✓ Logistics & Delivery (Amazon, FedEx, UPS)")
    print("✓ Manufacturing (Tesla, factories, robotics)")
    print("✓ Healthcare (scheduling, resource allocation)")
    print("✓ Energy Management (grid optimization)")
    print("✓ Warehouse Automation (inventory, picking)")
    print("\nSame agentic AI principles applied universally!")
    print("="*70)


if __name__ == "__main__":
    demo_multiple_industries()