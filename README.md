# Awesome Dark Kitchen Management Platforms

**Dark Kitchen Management Platforms** (also called cloud kitchen, ghost kitchen, or virtual brand platforms) help operators manage multi-brand delivery-only kitchens. They aggregate orders from multiple delivery apps (Uber Eats, DoorDash, Deliveroo, etc.), sync menus, route orders to the right station or brand, provide kitchen display systems (KDS), and streamline operations across virtual brands. Leading platforms include Otter, Deliverect, KitchenHub, Nextbite, Future Foods, CloudKitchens OS, Kitopi OS, POSist, UrbanPiper, and Local Kitchen Platform.

Below is a **curated list** of notable platforms and their open-source equivalents. Fully featured open-source alternatives that natively integrate with major delivery aggregators and support multi-brand dark kitchen workflows are still limited. Most open-source strength lies in restaurant ordering systems, kitchen display, POS, and customizable order management that can be extended for cloud-kitchen use cases.

## 🏢 SaaS / Hosted Platforms

- **[Otter](https://www.otter.ai/)** (or Otter.order) — Popular order aggregation and kitchen operations platform for multi-brand and multi-location restaurants.
- **[Deliverect](https://www.deliverect.com/)** — Leading middleware that connects delivery platforms with POS and kitchen systems; widely used by cloud kitchens.
- **[KitchenHub](https://www.kitchenhub.com/)**, **[Nextbite](https://www.nextbite.com/)**, **[Future Foods](https://www.futurefoods.io/)** — Specialized cloud kitchen and virtual brand management solutions.
- **[CloudKitchens OS](https://www.cloudkitchens.com/)**, **[Kitopi OS](https://www.kitopi.com/)**, **[POSist](https://www.posist.com/)**, **[UrbanPiper](https://www.urbanpiper.com/)**, **[Local Kitchen Platform](https://www.localkitchen.co/)** — Operator and technology platforms supporting dark kitchen networks and multi-brand execution.

## 🔓 Open-Source Software

### Open-Source Restaurant & Kitchen Management Systems
- **[KitchenAsty](https://github.com/mighty840/kitchenasty)** — Modern self-hosted restaurant ordering, reservation, and management system. Includes online ordering (delivery/pickup), menu management, kitchen display (Kanban-style), real-time updates, coupons, and admin analytics. MIT-licensed and built as a TypeScript monorepo — a strong foundation that can be adapted for dark kitchen workflows.
- Other open-source restaurant OS / POS projects that provide kitchen display systems (KDS), order routing, menu management, and multi-station support.
- Community restaurant management systems (often built on modern stacks or ERPNext/Odoo) that include KDS, inventory, and order handling.

### Order Aggregation & Multi-Channel Building Blocks
- Open-source multi-vendor food delivery platforms (customer + restaurant + driver apps) that can be customized for single-operator multi-brand use instead of marketplace mode.
- Self-hosted POS and ordering systems that support multiple order sources and can be integrated with delivery platform APIs via custom middleware.
- Kitchen Display System (KDS) focused open-source tools and real-time order boards that help manage high-volume delivery ticket flow.

### Supporting Open-Source Components
- Open-source inventory and recipe management tools useful for multi-brand ingredient tracking.
- Real-time communication and WebSocket frameworks for live order status across stations.
- Docker-based deployments that make it practical to run a private kitchen operations stack.

### Typical Open-Source Approach
1. **Core ordering & KDS** — KitchenAsty or similar self-hosted restaurant platform
2. **Menu & brand management** — Extended menu modules with virtual brand / station tagging
3. **Aggregator integration** — Custom middleware or lightweight connectors to delivery platforms (where APIs allow)
4. **Driver / handoff visibility** — Optional integration with open-source delivery or tracking tools
5. **Analytics** — Self-hosted dashboards on top of the order database

While this stack does not yet match the out-of-the-box multi-aggregator depth of Otter or Deliverect, it gives operators full data ownership, no per-order middleware fees, and the ability to tailor workflows specifically for multi-brand dark kitchen operations.

---

**How to contribute**  
Fork this repository, add a new project (with link + short description + category), and open a pull request.  
Prefer actively maintained open-source projects related to dark/cloud kitchen management, multi-brand order aggregation, kitchen display systems, or restaurant operations platforms.

**License**  
This list is public domain / CC0. Feel free to copy into your own awesome list or README.

Star the projects you find useful — open kitchen tools help operators run delivery brands more independently! 🍳
