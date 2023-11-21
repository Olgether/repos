from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Me(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="Имя", 
        help_text="Введите ваше имя")
    
    last_name = models.CharField(max_length=50, verbose_name="Фамилия", 
        help_text="Введите вашу фамилию")
    
    email = models.EmailField(verbose_name="Email", 
        help_text="Введите ваш действующий адрес электронной почты")
    
    phone = models.CharField(max_length=50, verbose_name="Телефон", 
        help_text="Введите ваш номер телефона")
    
    instagram = models.URLField(
        max_length=150, verbose_name="Instagram", blank=True, null=True, 
        help_text="Введите ваш профиль Instagram, если есть"
    )
    github = models.URLField(
        max_length=150, verbose_name="GitHub", blank=True, null=True, 
        help_text="Введите ваш профиль GitHub, если есть"
    )
    linkedin = models.URLField(
        max_length=150, verbose_name="LinkedIn", blank=True, null=True, 
        help_text="Введите ваш профиль LinkedIn, если есть"
    )
    telegram = models.URLField(
        max_length=150, verbose_name="Telegram", blank=True, null=True, 
        help_text="Введите ваш профиль Telegram, если есть"
    )
    
    education = models.TextField(verbose_name="Образование", blank=True, null=True, 
        help_text="Укажите вашу образовательную историю")
    
    work_history = models.TextField(verbose_name="Трудовая история", blank=True, null=True, 
        help_text="Укажите ваш опыт работы")

    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "Информация о себе"
        verbose_name_plural = "Информация о себе"


class Project(models.Model):
    file = models.FileField(upload_to="project_file/", blank=True, null=True, 
        help_text="Загрузите файл проекта, если необходимо")
    
    image = models.ImageField(upload_to="project_image/", blank=True, null=True, 
        help_text="Загрузите изображение проекта, если есть")
    
    title = models.CharField(max_length=150, verbose_name="Название проекта", 
        help_text="Введите название вашего проекта")
    
    description = models.TextField(verbose_name="Описание проекта", 
        help_text="Расскажите подробнее о вашем проекте")
    
    start_data = models.DateField(verbose_name="Дата начала", 
        help_text="Укажите дату начала проекта")
    end_data = models.DateField(verbose_name="Дата окончания", blank=True, null=True, 
        help_text="Укажите дату окончания проекта, если завершено")
    
    url = models.URLField(verbose_name="Ссылка на проект", blank=True, null=True, 
        help_text="Укажите ссылку на ваш проект, если есть")

    repository = models.URLField(verbose_name="Github Репозиторий", blank=True, null=True, 
        help_text="Укажите ссылку на репозиторий проекта на GitHub, если есть")
    
    technologies_used = models.CharField(max_length=100, verbose_name="Используемые технологии", 
        blank=True, null=True, help_text="Укажите технологии, используемые в проекте")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата последнего обновления")
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        ordering = ["-created_at"]
        

class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Программирование'),
        ('design', 'Дизайн'),
        ('languages', 'Языки программирования'),
        ('database', 'Базы данных'),
        ('frameworks', 'Фреймворки'),
        ('tools', 'Инструменты разработки'),
        ('soft_skills', 'Soft Skills'),
        ('web', 'Веб-разработка'),
        ('mobile', 'Мобильная разработка'),
        ('cloud', 'Облачные технологии'),
        ('testing', 'Тестирование и QA'),
        ('analytics', 'Аналитика данных'),
        ('machine_learning', 'Машинное обучение и искусственный интеллект'),
        ('security', 'Информационная безопасность'),
        ('networking', 'Сетевые технологии'),
        ('graphics', 'Графический дизайн'),
        ('audio_video', 'Аудио и видео производство'),
        ('project_management', 'Управление проектами'),
        ('communication', 'Коммуникационные навыки'),
        ('leadership', 'Лидерство'),
        ('entrepreneurship', 'Предпринимательство'),
        ('data_science', 'Наука о данных'),
        ('automation', 'Автоматизация процессов'),
        ('devops', 'DevOps'),
        ('blockchain', 'Блокчейн технологии'),
        ('robotics', 'Робототехника'),
    ]
    
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES,
        verbose_name="Категория", help_text="Выберите категорию для навыка")
    
    name = models.CharField(max_length=50, verbose_name="Навык", 
        help_text="Введите название вашего навыка")
    
    percentage = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name="Проценты", help_text="Введите ваш уровень в процентах")

    def __str__(self):
        return f"{self.name} ({self.percentage}%)"

    class Meta:
        verbose_name = "Навык"
        verbose_name_plural = "Навыки"
        

class Pricing(models.Model):
    service = models.CharField(max_length=100, verbose_name="Услуга", 
        help_text="Введите название услуги")
    description = models.TextField(verbose_name="Описание", 
        help_text="Добавьте краткое описание услуги")
    
    rate_per_hour = models.DecimalField(max_digits=10, decimal_places=2, 
        verbose_name="Ставка в час ($)", help_text="Укажите ставку в долларах за час работы")

    estimated_hours = models.DecimalField(max_digits=5, decimal_places=2, 
        verbose_name="Оценочное время работы (часы)", 
        help_text="Оцените, сколько часов требуется для выполнения услуги")

    def total_cost(self):
        """
        Метод total_cost вычисляет общую стоимость на основе почасовой ставки и расчетных часов.
        """
        return self.rate_per_hour * self.estimated_hours
    
    def __str__(self):
        return f"{self.service} - ${self.total_cost()}"

    class Meta:
        verbose_name = "Расценка"
        verbose_name_plural = "Расценки"
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя", 
        help_text="Введите ваше имя")
    
    email = models.EmailField(verbose_name="Email", 
        help_text="Введите ваш действующий адрес электронной почты")
    
    subject = models.CharField(max_length=200, verbose_name="Тема", 
        help_text="Введите тему вашего сообщения")
    message = models.TextField(verbose_name="Сообщение", 
        help_text="Оставьте ваше сообщение")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_read = models.BooleanField(default=False, verbose_name="Прочитано", 
        help_text="Отметьте, если сообщение было прочитано")

    def __str__(self):
        return f"{self.subject} - {self.name} - {self.email}"

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"