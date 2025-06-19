module.exports = {
  checkContent: (response, context, ee, next) => {
    if (response.body.includes("Blockbuster App")) {
      console.log("✓ Contenido HTML correcto");
    } else {
      console.log("✗ Contenido HTML no coincide");
    }
    return next();
  }
};