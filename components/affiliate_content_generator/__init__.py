from .modules.niche_identifier import NicheIdentifier
from .modules.product_scraper import ProductScraper
from .modules.content_generator import ContentGenerator
from .modules.seo_optimizer import SEOOptimizer
from .modules.conversion_booster import ConversionBooster
from .modules.analytics_tracker import AnalyticsTracker

class AACGSystem:
    def __init__(self, config):
        self.niche_identifier = NicheIdentifier(config)
        self.product_scraper = ProductScraper(config)
        self.content_generator = ContentGenerator(config)
        self.seo_optimizer = SEOOptimizer(config)
        self.conversion_booster = ConversionBooster(config)
        self.analytics_tracker = AnalyticsTracker(config)

    def process(self):
        niches = self.niche_identifier.identify_niches()
        for niche in niches:
            products = self.product_scraper.scrape_products(niche)
            content = self.content_generator.generate_content(niche, products)
            optimized_content = self.seo_optimizer.optimize(content)
            boosted_content = self.conversion_booster.boost(optimized_content)
            self.analytics_tracker.track(boosted_content)
```