#!/bin/bash
# Script para configurar el entorno (desarrollo o producción)

# Colores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}=== Configurador LSV GitHub Pages ===${NC}\n"

# Mostrar opciones
echo "Selecciona el entorno:"
echo "1) Desarrollo local (localhost:3000)"
echo "2) Producción (GitHub Pages)"
echo "3) Personalizado"
read -p "Opción (1-3): " option

# URLs base
DEV_BACKEND="http://localhost:3000"
DEV_BASE=""
PROD_BACKEND="https://api-lsv.tu-dominio.com"
PROD_BASE="https://usm-argenis.github.io/Avatar_LSV/"

# Seleccionar URLs
case $option in
  1)
    BACKEND_URL=$DEV_BACKEND
    BASE_URL=$DEV_BASE
    echo -e "${GREEN}✓ Configurado para desarrollo local${NC}"
    ;;
  2)
    BACKEND_URL=$PROD_BACKEND
    BASE_URL=$PROD_BASE
    echo -e "${YELLOW}⚠ Asegúrate de cambiar la URL del API en PROD_BACKEND${NC}"
    echo -e "${GREEN}✓ Configurado para GitHub Pages${NC}"
    ;;
  3)
    read -p "Backend URL: " BACKEND_URL
    read -p "Base URL (deja en blanco si es local): " BASE_URL
    echo -e "${GREEN}✓ Configuración personalizada guardada${NC}"
    ;;
  *)
    echo -e "${YELLOW}Opción inválida${NC}"
    exit 1
    ;;
esac

# Actualizar el archivo HTML
echo -e "\n${BLUE}Actualizando index.html...${NC}"

# Crear archivo temporal con las nuevas URLs
sed -i.bak "s|backendUrl:.*'http://localhost:3000'|backendUrl: '$BACKEND_URL'|g" index.html
sed -i.bak "s|? 'https://usm-argenis.github.io/Avatar_LSV/'|? '$BASE_URL'|g" index.html

rm -f index.html.bak

echo -e "${GREEN}✓ Backend URL: $BACKEND_URL${NC}"
echo -e "${GREEN}✓ Base URL: $BASE_URL${NC}"

# Mostrar instrucciones siguientes
echo -e "\n${BLUE}Próximos pasos:${NC}"
echo "1. Verifica que la configuración sea correcta"
echo "2. Prueba localmente: python -m http.server 8000"
echo "3. Si usas GitHub Pages, ejecuta: git add index.html && git commit -m 'Actualizar configuración API' && git push"

echo -e "\n${GREEN}✓ Configuración completada${NC}"
