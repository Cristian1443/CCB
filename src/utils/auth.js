/**
 * Verifica si el usuario está autenticado
 * Esta función se puede usar en la parte del cliente (navegador)
 */
export async function isAuthenticated() {
    try {
      const response = await fetch('/api/check-auth');
      if (response.ok) {
        const data = await response.json();
        return data.authenticated;
      }
      return false;
    } catch (error) {
      console.error('Error al verificar autenticación:', error);
      return false;
    }
  }
  
  /**
   * Obtiene la información del usuario actual
   */
  export async function getCurrentUser() {
    try {
      const response = await fetch('/api/check-auth');
      if (response.ok) {
        const data = await response.json();
        return data.user;
      }
      return null;
    } catch (error) {
      console.error('Error al obtener usuario:', error);
      return null;
    }
  }
  
  /**
   * Middleware para proteger rutas en Astro
   * Esta función se usa en la parte del servidor (SSR)
   */
  export async function protectRoute(context, allowedRoles = null) {
    // Verificar si hay un usuario en la sesión (esto requiere integración con Flask)
    try {
      const response = await fetch('http://localhost:5000/api/check-auth', {
        headers: {
          cookie: context.request.headers.get('cookie') || ''
        }
      });
      
      if (!response.ok) {
        return context.redirect('/login');
      }
      
      const data = await response.json();
      
      // Verificar si el rol es permitido (si se especificó)
      if (allowedRoles && !allowedRoles.includes(data.user.role)) {
        return context.redirect('/unauthorized');
      }
      
      // Devolver los datos del usuario para usar en la página
      return data.user;
    } catch (error) {
      console.error('Error en protectRoute:', error);
      return context.redirect('/login');
    }
  }
  
  /**
   * Cierra la sesión del usuario
   */
  export async function logout() {
    try {
      const response = await fetch('/api/logout', {
        method: 'POST',
      });
      
      if (response.ok) {
        const data = await response.json();
        window.location.href = data.redirect;
      }
    } catch (error) {
      console.error('Error al cerrar sesión:', error);
    }
  }