from django.db import models

# 3.2 버전 이후로는 자동으로 id가 bigint 설정됨
class Artwork(models.Model):
    title = models.CharField(max_length=255)
    img_url = models.URLField(max_length=500)  # URLField 사용 권장
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
