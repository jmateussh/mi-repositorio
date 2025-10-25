import discord
from discord.ext import commands
from ficheros import evaluar_objeto
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
@bot.command()
async def reciclar(ctx, *, objeto):
    respuesta = evaluar_objeto(objeto)
    await ctx.send(respuesta)
# Reemplaza
bot.run("")
OBJETOS = {
    "botella de plástico": {
        "reciclable": True,
        "tiempo_descomposicion": "450 años"
    },
    "bolsa de plástico": {
        "reciclable": True,
        "tiempo_descomposicion": "10-20 años"
    },
    "caja de cartón": {
        "reciclable": True,
        "tiempo_descomposicion": "2 meses"
    },
    "cepillo de dientes": {
        "reciclable": False,
        "tiempo_descomposicion": "500 años",
        "manualidad": "puedes usarlo para limpiar esquinas o teclados difíciles"
    },
    "envase de yogur": {
        "reciclable": True,
        "tiempo_descomposicion": "30-50 años"
    }
}
def evaluar_objeto(nombre_objeto):  
    # Convierte el nombre del objeto a minúsculas para evitar errores con mayúsculas/minúsculas
    nombre_objeto = nombre_objeto.lower()  

    # Verifica si el objeto existe dentro del diccionario OBJETOS
    if nombre_objeto not in OBJETOS:
        # Si no existe, devuelve un mensaje indicando los objetos disponibles
        return f"No conozco ese objeto. Intenta con estos {list(OBJETOS.keys())}"

    # Obtiene los datos del objeto desde el diccionario OBJETOS
    datos = OBJETOS[nombre_objeto]

    # Verifica si el objeto es reciclable
    if datos["reciclable"] == True:
        accion = "RECICLAR"  # Si es reciclable, la acción será reciclar
    else:
        accion = "DALE UN NUEVO USO"  # Si no lo es, sugiere una manualidad

    # Construye el mensaje con la información básica del objeto
    resultado = f"🔍 OBJETO: {nombre_objeto}\n"
    resultado += f"♻️ ACCIÓN: {accion}\n"
    resultado += f"⏳ TIEMPO DE DESCOMPOSICIÓN: {datos['tiempo_descomposicion']}\n"

    # Si el objeto no es reciclable y además tiene una sugerencia de manualidad, la agrega al resultado
    if not datos["reciclable"] and "manualidad" in datos:
        resultado += f"🎨 SUGERENCIA: {datos['manualidad']}\n"

    # Retorna el mensaje final con toda la información procesada
    return resultado

# Ejemplo de uso: imprime la evaluación de "botella de plástico"
print(evaluar_objeto("ladrillo"))
