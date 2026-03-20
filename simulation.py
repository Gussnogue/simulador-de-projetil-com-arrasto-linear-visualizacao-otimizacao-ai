import numpy as np

def simulate_projectile(v0, angle_deg, mass, k, dt=0.01, t_max=20):
    """
    Simula projétil com arrasto linear usando método de Euler.
    
    Parâmetros:
        v0: velocidade inicial (m/s)
        angle_deg: ângulo em graus
        mass: massa (kg)
        k: coeficiente de arrasto linear (N·s/m)
        dt: passo de tempo (s)
        t_max: tempo máximo de simulação (s)
    
    Retorna:
        t: array de tempos
        x, y: arrays das posições
        vx, vy: arrays das velocidades
        range_max: alcance horizontal máximo (m)
        flight_time: tempo de voo (s)
    """
    g = 9.81
    angle_rad = np.radians(angle_deg)
    vx = v0 * np.cos(angle_rad)
    vy = v0 * np.sin(angle_rad)
    
    # Listas para armazenar histórico
    t_vals = [0.0]
    x_vals = [0.0]
    y_vals = [0.0]
    vx_vals = [vx]
    vy_vals = [vy]
    
    t = 0.0
    while t < t_max and y_vals[-1] >= 0:
        # Acelerações
        ax = - (k / mass) * vx
        ay = -g - (k / mass) * vy
        
        # Euler
        vx += ax * dt
        vy += ay * dt
        x = x_vals[-1] + vx * dt
        y = y_vals[-1] + vy * dt
        t += dt
        
        # Armazenar
        t_vals.append(t)
        x_vals.append(x)
        y_vals.append(y)
        vx_vals.append(vx)
        vy_vals.append(vy)
    
    # Remove último ponto se entrou no solo (y < 0)
    if y_vals[-1] < 0:
        t_vals.pop()
        x_vals.pop()
        y_vals.pop()
        vx_vals.pop()
        vy_vals.pop()
    
    # Converte para arrays
    t_arr = np.array(t_vals)
    x_arr = np.array(x_vals)
    y_arr = np.array(y_vals)
    vx_arr = np.array(vx_vals)
    vy_arr = np.array(vy_vals)
    
    # Alcance e tempo de voo
    range_max = x_arr[-1] if len(x_arr) > 0 else 0.0
    flight_time = t_arr[-1] if len(t_arr) > 0 else 0.0
    
    return t_arr, x_arr, y_arr, vx_arr, vy_arr, range_max, flight_time

