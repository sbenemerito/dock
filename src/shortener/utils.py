import random, string


def generate_code(size=6, chars=string.ascii_lowercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))


def create_shortcode(instance, size=6):
	inheritedClass = instance.__class__
	new_code = generate_code(size=size)
	qs_exists = inheritedClass.objects.filter(shortcode=new_code).exists()

	if qs_exists:
		return create_shortcode(size=size)
	return new_code

