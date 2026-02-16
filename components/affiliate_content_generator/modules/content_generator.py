import logging
from typing import Dict, Any
from jinja2 import Template

class ContentGenerator:
    def __init__(self, config):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)
        self.template = Template(self.config['content_template'])

    def generate_content(self, niche: str, products: List[Dict]) -> Dict:
        """
        Generates SEO-friendly content using a template.
        Returns the generated content as a dictionary.
        """
        try:
            content = self.template.render({
                'niche': niche,
                'products': products
            })
            return {'content': content}
        except Exception as e:
            self.logger.error(f"Content generation failed: {str(e)}")
            return {}