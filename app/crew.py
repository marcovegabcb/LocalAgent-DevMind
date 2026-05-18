from crewai import Crew, Process
# Importación de agentes
from app.agents.analyst import create_analyst_agent
from app.agents.optimizer import create_optimizer_agent
from app.agents.planner import create_planner_agent  
from app.agents.seeker import create_seeker_agent    
from app.agents.writer import create_writer_agent

# Importación de tareas
from app.tasks.analysis_tasks import create_analysis_task
from app.tasks.optimizing_tasks import create_optimization_task
from app.tasks.planning_tasks import create_planner_task    
from app.tasks.searching_tasks import create_seeker_task   
from app.tasks.writing_tasks import create_writing_task


# ==========================================
# FASE 1: GENERADOR DEL README
# ==========================================
def run_documenter_crew(
    m_analyst, m_planner, m_seeker, m_writer,
    t_analyst, t_planner, t_seeker, t_writer,
    language, code, file_name,
    status_callback, end_callback
):
    """
    Fase 1: Orquesta el análisis técnico y la redacción del README.md.
    Libera el control y el resultado inmediatamente al terminar.
    """
    # 1. Instanciar Agentes de la primera fase
    analyst = create_analyst_agent(m_analyst, language, t_analyst)
    planner = create_planner_agent(m_planner, language, t_planner)
    seeker = create_seeker_agent(m_seeker, language, t_seeker) 
    writer = create_writer_agent(m_writer, language, t_writer)

    # 2. Configurar Tareas de la primera fase
    t1 = create_analysis_task(analyst, code, language)
    t1.callback = end_callback

    t2_plan = create_planner_task(planner, t1, language)
    t2_plan.callback = end_callback

    t3_search = create_seeker_task(seeker, t2_plan, language)
    t3_search.callback = end_callback

    t4_write = create_writing_task(writer, [t1, t3_search], language)
    t4_write.callback = end_callback

    # 3. Formar la Crew de Documentación
    documenter_crew = Crew(
        agents=[analyst, planner, seeker, writer], 
        tasks=[t1, t2_plan, t3_search, t4_write], 
        process=Process.sequential,
        verbose=True
    )
    
    # 4. Lanzar
    status_callback("⚡ System", "Launching documentation workflow...", "#34495e")
    documenter_crew.kickoff()
    status_callback("✅ System", "README generated successfully!", "#2ecc71")
    
    # Devolvemos única y exclusivamente el texto del README
    return str(t4_write.output)


# ==========================================
# FASE 2: AUDITORÍA DE OPTIMIZACIONES
# ==========================================
def run_optimizer_crew(
    m_optimizer, t_optimizer,
    language, code, file_name,
    status_callback, end_callback
):
    """
    Fase 2: Ejecuta de forma aislada y limpia el agente optimizador 
    para evitar saturación de contexto y colisiones de VRAM.
    """
    # 1. Instanciar el Agente Optimizador
    optimizer = create_optimizer_agent(m_optimizer, language, t_optimizer)

    # 2. Configurar la Tarea del Optimizador
    t5_optimize = create_optimization_task(optimizer, code, language)
    t5_optimize.callback = end_callback

    # 3. Formar la Crew de Optimización (Un solo agente especializado)
    optimizer_crew = Crew(
        agents=[optimizer],
        tasks=[t5_optimize],
        process=Process.sequential,
        verbose=True
    )

    # 4. Lanzar
    status_callback("🔮 System", "Analyzing code efficiency and architecture...", "#6c5ce7")
    optimizer_crew.kickoff()
    status_callback("✅ System", "Code optimization analysis completed!", "#2ecc71")

    # Devolvemos el feedback de optimización limpio
    return str(t5_optimize.output)