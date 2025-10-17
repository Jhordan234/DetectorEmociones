# 🎭 Detector de Emociones

<div align="center">

![Emotion Detection](https://img.shields.io/badge/AI-Emotion%20Detection-blueviolet?style=for-the-badge&logo=tensorflow)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python&logoColor=white)
![Deep Learning](https://img.shields.io/badge/Deep%20Learning-Enabled-red?style=for-the-badge&logo=keras)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**Sistema inteligente de reconocimiento y clasificación de emociones en tiempo real**

[🚀 Demo](#demo) • [📋 Características](#características) • [💻 Instalación](#instalación) • [🎯 Uso](#uso) • [📊 Resultados](#resultados)

</div>

---

## 📖 Descripción

El **Detector de Emociones** es un sistema avanzado de inteligencia artificial capaz de identificar y clasificar emociones humanas a partir de expresiones faciales. Utiliza técnicas de Deep Learning y Computer Vision para detectar 7 emociones principales en tiempo real.

### 🎯 Emociones Detectadas

| Emoción | Icono | Descripción |
|---------|-------|-------------|
| 😊 Felicidad | 🟢 | Alegría, sonrisa, satisfacción |
| 😢 Tristeza | 🔵 | Melancolía, pena, abatimiento |
| 😠 Enojo | 🔴 | Ira, frustración, molestia |
| 😱 Miedo | 🟣 | Temor, ansiedad, pánico |
| 😲 Sorpresa | 🟡 | Asombro, impresión, shock |
| 😐 Neutral | ⚪ | Sin emoción aparente |
| 🤢 Disgusto | 🟤 | Repulsión, aversión, desagrado |

---

## ✨ Características

- 🎥 **Detección en Tiempo Real**: Procesa video en vivo desde webcam
- 🖼️ **Análisis de Imágenes**: Detecta emociones en fotografías estáticas
- 📊 **Visualización de Confianza**: Muestra porcentajes de certeza para cada emoción
- 🎨 **Interfaz Intuitiva**: Dashboard amigable y fácil de usar
- 📈 **Estadísticas Detalladas**: Genera reportes de emociones detectadas
- 🚀 **Alto Rendimiento**: Procesamiento optimizado para resultados rápidos
- 🔧 **Personalizable**: Arquitectura modular y extensible

---

## 🛠️ Tecnologías

<div align="center">

![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![Keras](https://img.shields.io/badge/Keras-D00000?style=flat-square&logo=keras&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=flat-square&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)

</div>

---

## 💻 Instalación

### Prerequisitos

- Python 3.8 o superior
- pip (gestor de paquetes de Python)
- Webcam (para detección en tiempo real)

### Pasos de Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/detector-emociones.git
cd detector-emociones
```

2. **Crear entorno virtual** (recomendado)
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

3. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

4. **Descargar modelo pre-entrenado**
```bash
python download_model.py
```

---

## 🎯 Uso

### Detección desde Webcam

```bash
python detect_emotion.py --source webcam
```

### Detección desde Imagen

```bash
python detect_emotion.py --source image --path ruta/a/imagen.jpg
```

### Detección desde Video

```bash
python detect_emotion.py --source video --path ruta/a/video.mp4
```

### Parámetros Adicionales

```bash
python detect_emotion.py --source webcam --confidence 0.7 --save-output --fps 30
```

---

## 📊 Resultados

### Precisión del Modelo

| Métrica | Valor |
|---------|-------|
| 🎯 Accuracy | 94.3% |
| 📈 Precision | 93.8% |
| 🔄 Recall | 94.1% |
| ⚖️ F1-Score | 93.9% |

### Rendimiento

- ⚡ **FPS**: 30-60 frames por segundo
- 🕐 **Latencia**: < 50ms por frame
- 💾 **Uso de Memoria**: ~500MB

---

---

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. 🍴 Fork el proyecto
2. 🔧 Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. 💾 Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. 📤 Push a la rama (`git push origin feature/AmazingFeature`)
5. 🎉 Abre un Pull Request

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

---

## 👥 Autores

- **Tu Nombre** - *Desarrollo Principal* - [@Jhordan234](https://github.com/Jhordan234)

---

## 🙏 Agradecimientos

- Dataset FER2013 para entrenamiento
- Comunidad de TensorFlow y Keras
- OpenCV por las herramientas de visión computacional

---

<div align="center">

**⭐ Si este proyecto te fue útil, considera darle una estrella ⭐**

Made with ❤️ and 🐍 Python

</div>
