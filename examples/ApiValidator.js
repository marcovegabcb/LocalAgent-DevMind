/**
 * Validador simple para peticiones de usuario
 */
const validateUser = (data) => {
    const errors = [];
    
    if (!data.username || data.username.length < 3) {
        errors.push("El nombre de usuario debe tener al menos 3 caracteres.");
    }
    
    if (!data.email || !data.email.includes("@")) {
        errors.push("Formato de email inválido.");
    }

    return {
        isValid: errors.length === 0,
        errors: errors
    };
};

const userData = { username: "Al", email: "correo-sin-arroba" };
const result = validateUser(userData);
console.log("Resultado de validación:", result);
