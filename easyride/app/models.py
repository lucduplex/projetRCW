from django.db import models
from django.contrib.auth.models import User
import face_recognition

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    face_encoding = models.TextField(null=True, blank=True)  # Stocker le descripteur facial

    def save_face_encoding(self, image):
        # Convertit l'image en descripteur facial
        face_image = face_recognition.load_image_file(image)
        face_encodings = face_recognition.face_encodings(face_image)
        if face_encodings:
            self.face_encoding = ','.join(map(str, face_encodings[0]))
            self.save()

    def verify_face(self, image):
        # Vérifie si l'image fournie correspond au descripteur stocké
        face_image = face_recognition.load_image_file(image)
        face_encodings = face_recognition.face_encodings(face_image)
        if face_encodings:
            user_face_encoding = list(map(float, self.face_encoding.split(',')))
            return face_recognition.compare_faces([user_face_encoding], face_encodings[0])[0]
        return False