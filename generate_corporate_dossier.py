#!/usr/bin/env python3
import base64
import os

with open('/Volumes/Work/backup/HOTEL-FOZ-DO-IGUACU/logo_spa_do_colchao.png', 'rb') as f:
    logo_base64 = base64.b64encode(f.read()).decode('utf-8')
logo_data_uri = f"data:image/png;base64,{logo_base64}"

html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Dossiê Técnico & Proposta Comercial Corporativa — Hotel Foz do Iguaçu</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
    <style>
        :root {{
            --navy-dark: #09172a;
            --navy-corporate: #0f233d;
            --teal-brand: #155e75;
            --teal-subtle: #ecfeff;
            --teal-border: #a5f3fc;
            --gold-accent: #b45309;
            --gold-subtle: #fffbeb;
            --gold-border: #fde68a;
            --slate-text: #0f172a;
            --slate-secondary: #334155;
            --slate-muted: #64748b;
            --border-light: #e2e8f0;
            --border-dark: #cbd5e1;
            --bg-page: #ffffff;
            --bg-card: #f8fafc;
            --font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: var(--font-family);
            background-color: #cbd5e1;
            color: var(--slate-text);
            -webkit-font-smoothing: antialiased;
            -moz-osx-font-smoothing: grayscale;
            margin: 0;
            padding: 20px 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 24px;
        }}

        /* PÁGINAS A4 RETRATO EXATAS (210mm x 297mm) */
        .page-a4 {{
            width: 210mm;
            height: 297mm;
            min-height: 297mm;
            max-height: 297mm;
            background: var(--bg-page);
            padding: 16mm 18mm 14mm 18mm;
            position: relative;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.12);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            page-break-after: always;
            break-after: page;
        }}

        .page-a4:last-of-type {{
            page-break-after: avoid;
            break-after: avoid;
        }}

        /* ================= PÁGINA 1: CAPA CORPORATIVA DE LUXO ================= */
        .cover-page {{
            padding: 0 !important;
            background: radial-gradient(circle at 85% 15%, rgba(21, 94, 117, 0.4) 0%, rgba(9, 23, 42, 0.98) 65%), #09172a !important;
            color: #ffffff !important;
            position: relative;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }}

        .cover-top-bar {{
            padding: 18mm 20mm 10mm 20mm;
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid rgba(255, 255, 255, 0.12);
        }}

        .cover-logo-capsule {{
            background: #ffffff;
            padding: 10px 18px;
            border-radius: 8px;
            display: inline-flex;
            align-items: center;
            box-shadow: 0 4px 15px rgba(0, 0, 0, 0.25);
        }}

        .cover-logo-img {{
            height: 32px;
            width: auto;
        }}

        .cover-process-tag {{
            font-size: 10px;
            font-weight: 800;
            letter-spacing: 1px;
            text-transform: uppercase;
            color: #a5f3fc;
            text-align: right;
            line-height: 1.4;
        }}

        .cover-process-tag span {{
            color: #ffffff;
            font-weight: 900;
        }}

        .cover-center-block {{
            padding: 12mm 20mm 10mm 20mm;
            display: flex;
            flex-direction: column;
            justify-content: center;
            flex: 1;
        }}

        .cover-badge-category {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            background: rgba(21, 94, 117, 0.35);
            border: 1px solid rgba(165, 243, 252, 0.4);
            color: #67e8f9;
            font-size: 10.5px;
            font-weight: 800;
            letter-spacing: 1.2px;
            text-transform: uppercase;
            padding: 5px 14px;
            border-radius: 20px;
            margin-bottom: 16px;
            align-self: flex-start;
        }}

        .cover-main-h1 {{
            font-size: 34px;
            font-weight: 900;
            line-height: 1.15;
            letter-spacing: -0.8px;
            color: #ffffff;
            margin-bottom: 12px;
            max-width: 620px;
            text-wrap: balance;
        }}

        .cover-lead-p {{
            font-size: 14px;
            line-height: 1.55;
            color: #cbd5e1;
            margin-bottom: 28px;
            max-width: 580px;
            text-wrap: balance;
        }}

        .cover-recipient-card {{
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.15);
            backdrop-filter: blur(8px);
            -webkit-backdrop-filter: blur(8px);
            border-radius: 8px;
            padding: 16px 20px;
            max-width: 580px;
            border-left: 4px solid #38bdf8;
        }}

        .cover-recipient-label {{
            font-size: 9.5px;
            font-weight: 800;
            letter-spacing: 0.8px;
            text-transform: uppercase;
            color: #94a3b8;
            margin-bottom: 4px;
            display: block;
        }}

        .cover-recipient-name {{
            font-size: 18px;
            font-weight: 900;
            color: #ffffff;
            letter-spacing: -0.3px;
            margin-bottom: 2px;
        }}

        .cover-recipient-sub {{
            font-size: 11.5px;
            color: #e2e8f0;
            line-height: 1.4;
        }}

        .cover-bottom-bar {{
            padding: 12mm 20mm 16mm 20mm;
            border-top: 1px solid rgba(255, 255, 255, 0.12);
            background: rgba(0, 0, 0, 0.2);
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .cover-footer-meta {{
            font-size: 10.5px;
            color: #94a3b8;
            line-height: 1.45;
        }}

        .cover-footer-meta strong {{
            color: #ffffff;
        }}

        .cover-badges-right {{
            display: flex;
            gap: 8px;
        }}

        .cover-badge-pill {{
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #ffffff;
            font-size: 9.5px;
            font-weight: 800;
            padding: 4px 10px;
            border-radius: 14px;
            letter-spacing: 0.4px;
            text-transform: uppercase;
        }}

        /* ================= PÁGINAS INTERNAS (PÁG 2 A 8) ================= */
        .doc-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1.5px solid var(--border-light);
            padding-bottom: 10px;
            margin-bottom: 16px;
            flex-shrink: 0;
        }}

        .doc-header-brand {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}

        .doc-logo {{
            height: 30px;
            width: auto;
        }}

        .doc-division-badge {{
            font-size: 10px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            color: var(--teal-brand);
            background: var(--teal-subtle);
            border: 1px solid var(--teal-border);
            padding: 3px 8px;
            border-radius: 4px;
        }}

        .doc-header-meta {{
            font-size: 10.5px;
            color: var(--slate-muted);
            text-align: right;
            line-height: 1.35;
            font-variant-numeric: tabular-nums;
        }}

        .doc-header-meta strong {{
            color: var(--navy-dark);
        }}

        .doc-footer {{
            border-top: 1px solid var(--border-light);
            padding-top: 8px;
            margin-top: 14px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            font-size: 9.5px;
            color: var(--slate-muted);
            flex-shrink: 0;
        }}

        .doc-footer-company {{
            font-weight: 600;
        }}

        .doc-footer-page {{
            font-weight: 800;
            color: var(--navy-dark);
        }}

        .page-body {{
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: flex-start;
            min-height: 0;
        }}

        .section-eyebrow {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 10px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.8px;
            color: var(--teal-brand);
            margin-bottom: 6px;
        }}

        .section-title {{
            font-size: 20px;
            font-weight: 900;
            color: var(--navy-dark);
            letter-spacing: -0.4px;
            margin-bottom: 6px;
            line-height: 1.25;
            text-wrap: balance;
        }}

        .section-lead {{
            font-size: 12px;
            color: var(--slate-secondary);
            line-height: 1.5;
            margin-bottom: 16px;
            text-wrap: balance;
        }}

        /* CADASTRO (PÁG 2) */
        .cadastral-card {{
            background: var(--bg-card);
            border: 1.5px solid var(--border-light);
            border-radius: 8px;
            padding: 16px 20px;
            margin-bottom: 20px;
        }}

        .cadastral-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 16px 24px;
        }}

        .cadastral-item {{
            display: flex;
            flex-direction: column;
            gap: 3px;
        }}

        .cadastral-label {{
            font-size: 9.5px;
            text-transform: uppercase;
            font-weight: 800;
            letter-spacing: 0.5px;
            color: var(--slate-muted);
        }}

        .cadastral-val {{
            font-size: 13px;
            font-weight: 700;
            color: var(--navy-dark);
        }}

        .metrics-grid-3 {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 14px;
            margin-bottom: 20px;
        }}

        .metric-card {{
            background: #ffffff;
            border: 1px solid var(--border-light);
            border-radius: 8px;
            padding: 16px;
            border-top: 3.5px solid var(--teal-brand);
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.04);
        }}

        .metric-card.gold {{
            border-top-color: var(--gold-accent);
        }}

        .metric-val {{
            font-size: 22px;
            font-weight: 900;
            color: var(--navy-dark);
            margin-bottom: 4px;
            font-variant-numeric: tabular-nums;
        }}

        .metric-title {{
            font-size: 11.5px;
            font-weight: 800;
            color: var(--slate-secondary);
            margin-bottom: 4px;
        }}

        .metric-desc {{
            font-size: 10px;
            color: var(--slate-muted);
            line-height: 1.4;
        }}

        /* CARTA FORMAL (PÁG 3) */
        .letter-recipient {{
            background: var(--bg-card);
            border-left: 3px solid var(--teal-brand);
            padding: 12px 16px;
            border-radius: 0 6px 6px 0;
            margin-bottom: 18px;
            font-size: 11.5px;
            color: var(--slate-secondary);
            line-height: 1.45;
        }}

        .letter-text {{
            font-size: 11.5px;
            color: var(--slate-secondary);
            line-height: 1.65;
            margin-bottom: 14px;
            text-align: justify;
        }}

        .pillars-grid-4 {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 12px;
            margin-top: 10px;
        }}

        .pillar-card {{
            background: #ffffff;
            border: 1px solid var(--border-light);
            border-radius: 6px;
            padding: 12px 14px;
        }}

        .pillar-header {{
            display: flex;
            align-items: center;
            gap: 8px;
            margin-bottom: 4px;
        }}

        .pillar-badge {{
            width: 22px;
            height: 22px;
            border-radius: 4px;
            background: var(--teal-subtle);
            color: var(--teal-brand);
            font-size: 10.5px;
            font-weight: 900;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .pillar-title {{
            font-size: 11.5px;
            font-weight: 800;
            color: var(--navy-dark);
        }}

        .pillar-desc {{
            font-size: 10px;
            color: var(--slate-muted);
            line-height: 1.4;
        }}

        /* ESPECIFICAÇÕES (PÁG 4) */
        .specs-grid {{
            display: grid;
            grid-template-columns: 1fr;
            gap: 12px;
        }}

        .spec-box {{
            background: #ffffff;
            border: 1px solid var(--border-light);
            border-radius: 6px;
            padding: 12px 16px;
            display: grid;
            grid-template-columns: 36px 1fr 140px;
            gap: 14px;
            align-items: center;
        }}

        .spec-box.recommended {{
            border-color: var(--teal-brand);
            background: #fafefd;
            box-shadow: 0 1px 4px rgba(21, 94, 117, 0.08);
        }}

        .spec-index {{
            width: 32px;
            height: 32px;
            border-radius: 6px;
            background: var(--navy-dark);
            color: #ffffff;
            font-size: 12.5px;
            font-weight: 900;
            display: flex;
            align-items: center;
            justify-content: center;
        }}

        .spec-content h4 {{
            font-size: 12.5px;
            font-weight: 800;
            color: var(--navy-dark);
            margin-bottom: 3px;
        }}

        .spec-content p {{
            font-size: 10.5px;
            color: var(--slate-secondary);
            line-height: 1.4;
        }}

        .spec-meta {{
            text-align: right;
            border-left: 1px solid var(--border-light);
            padding-left: 12px;
        }}

        .spec-meta-dim {{
            font-size: 11px;
            font-weight: 800;
            color: var(--navy-dark);
        }}

        .spec-meta-tag {{
            font-size: 9.5px;
            font-weight: 700;
            color: var(--teal-brand);
            margin-top: 2px;
        }}

        /* TABELAS (PÁG 5) */
        .table-corporate {{
            width: 100%;
            border-collapse: collapse;
            font-size: 11px;
            margin-bottom: 16px;
            border: 1px solid var(--border-light);
            border-radius: 6px;
            overflow: hidden;
        }}

        .table-corporate th {{
            background: var(--navy-dark);
            color: #ffffff;
            font-size: 10px;
            font-weight: 800;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            padding: 9px 12px;
            text-align: left;
            border-bottom: 1px solid var(--border-light);
        }}

        .table-corporate td {{
            padding: 9px 12px;
            border-bottom: 1px solid var(--border-light);
            color: var(--slate-secondary);
            vertical-align: middle;
        }}

        .table-corporate tr:nth-child(even) {{
            background: #f8fafc;
        }}

        .table-corporate tr:last-child td {{
            border-bottom: none;
        }}

        .price-bold {{
            font-weight: 800;
            color: var(--navy-dark);
            font-variant-numeric: tabular-nums;
        }}

        .price-highlight {{
            font-weight: 900;
            color: var(--teal-brand);
            font-variant-numeric: tabular-nums;
        }}

        .savings-tag {{
            display: inline-block;
            background: #f0fdf4;
            color: #166534;
            border: 1px solid #bbf7d0;
            padding: 2px 7px;
            border-radius: 4px;
            font-size: 9.5px;
            font-weight: 800;
            font-variant-numeric: tabular-nums;
        }}

        /* COMBOS (PÁG 6) */
        .combos-container {{
            display: flex;
            flex-direction: column;
            gap: 12px;
            margin-bottom: 14px;
        }}

        .combo-row {{
            background: #ffffff;
            border: 1.5px solid var(--border-light);
            border-radius: 6px;
            padding: 14px 18px;
            display: grid;
            grid-template-columns: 1fr 220px;
            gap: 16px;
            align-items: center;
        }}

        .combo-row.highlighted {{
            border-color: var(--teal-brand);
            background: linear-gradient(90deg, #ffffff 0%, var(--teal-subtle) 100%);
        }}

        .combo-info h4 {{
            font-size: 13.5px;
            font-weight: 900;
            color: var(--navy-dark);
            margin-bottom: 4px;
        }}

        .combo-info p {{
            font-size: 11px;
            color: var(--slate-secondary);
            line-height: 1.45;
        }}

        .combo-values {{
            background: #ffffff;
            border: 1px solid var(--border-light);
            border-radius: 6px;
            padding: 10px 14px;
            text-align: right;
        }}

        .combo-de {{
            font-size: 10px;
            color: var(--slate-muted);
            text-decoration: line-through;
            font-variant-numeric: tabular-nums;
        }}

        .combo-por {{
            font-size: 17px;
            font-weight: 900;
            color: var(--teal-brand);
            font-variant-numeric: tabular-nums;
        }}

        .combo-eco {{
            font-size: 10px;
            font-weight: 800;
            color: #166534;
        }}

        .master-banner {{
            background: var(--navy-dark);
            color: #ffffff;
            border-radius: 6px;
            padding: 14px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .master-banner-title {{
            font-size: 12.5px;
            font-weight: 800;
            letter-spacing: 0.3px;
            text-transform: uppercase;
        }}

        .master-banner-sub {{
            font-size: 10.5px;
            color: #94a3b8;
            margin-top: 2px;
        }}

        .master-banner-price {{
            font-size: 21px;
            font-weight: 900;
            color: #38bdf8;
            font-variant-numeric: tabular-nums;
        }}

        /* LOGÍSTICA (PÁG 7) */
        .flow-grid-4 {{
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 12px;
            margin-bottom: 16px;
        }}

        .flow-step {{
            background: var(--bg-card);
            border: 1px solid var(--border-light);
            border-radius: 6px;
            padding: 12px 10px;
            border-top: 3px solid var(--teal-brand);
        }}

        .flow-step-num {{
            font-size: 10.5px;
            font-weight: 900;
            color: var(--teal-brand);
            margin-bottom: 4px;
        }}

        .flow-step-title {{
            font-size: 11px;
            font-weight: 800;
            color: var(--navy-dark);
            margin-bottom: 4px;
        }}

        .flow-step-desc {{
            font-size: 9.5px;
            color: var(--slate-secondary);
            line-height: 1.4;
        }}

        .sla-box {{
            background: #ffffff;
            border: 1px solid var(--border-light);
            border-radius: 6px;
            padding: 14px 18px;
            margin-bottom: 14px;
        }}

        .sla-box h4 {{
            font-size: 12px;
            font-weight: 800;
            color: var(--navy-dark);
            margin-bottom: 8px;
        }}

        .sla-box ul {{
            padding-left: 20px;
            font-size: 10.5px;
            color: var(--slate-secondary);
            line-height: 1.55;
        }}

        /* ASSINATURAS (PÁG 8) */
        .formal-clauses {{
            background: var(--bg-card);
            border: 1px solid var(--border-light);
            border-radius: 6px;
            padding: 14px 18px;
            font-size: 10.5px;
            color: var(--slate-secondary);
            line-height: 1.55;
            margin-bottom: 16px;
        }}

        .formal-clauses ol {{
            padding-left: 18px;
        }}

        .formal-clauses li {{
            margin-bottom: 6px;
        }}

        .acceptance-box {{
            border: 1.5px solid var(--teal-brand);
            border-radius: 6px;
            padding: 16px 20px;
            margin-bottom: 20px;
            background: #ffffff;
        }}

        .acceptance-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 14px;
            margin-top: 10px;
        }}

        .acc-field {{
            border-bottom: 1px solid var(--border-dark);
            padding-bottom: 4px;
            font-size: 10.5px;
            color: var(--slate-secondary);
        }}

        .acc-field strong {{
            font-size: 9.5px;
            text-transform: uppercase;
            color: var(--slate-muted);
            display: block;
            margin-bottom: 3px;
        }}

        .signatures-grid {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 36px;
            margin-top: 28px;
            padding-top: 12px;
        }}

        .sig-block {{
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
        }}

        .sig-line {{
            width: 100%;
            border-top: 1.5px solid var(--navy-dark);
            margin-bottom: 8px;
        }}

        .sig-name {{
            font-size: 11.5px;
            font-weight: 800;
            color: var(--navy-dark);
        }}

        .sig-role {{
            font-size: 10px;
            color: var(--slate-muted);
            margin-bottom: 3px;
        }}

        .sig-company {{
            font-size: 9.5px;
            font-weight: 700;
            color: var(--teal-brand);
        }}

        /* ESTILOS DE IMPRESSÃO / PDF */
        @page {{
            size: A4 portrait;
            margin: 0;
        }}

        @media print {{
            body {{
                background: #ffffff !important;
                padding: 0 !important;
                gap: 0 !important;
            }}

            .page-a4 {{
                box-shadow: none !important;
                margin: 0 !important;
                width: 210mm !important;
                height: 297mm !important;
                min-height: 297mm !important;
                max-height: 297mm !important;
                page-break-after: always !important;
                break-after: page !important;
                page-break-inside: avoid !important;
                break-inside: avoid !important;
            }}

            .page-a4:last-of-type {{
                page-break-after: avoid !important;
                break-after: avoid !important;
            }}
        }}
    </style>
</head>
<body>

    <!-- ================= PÁGINA 1: CAPA CORPORATIVA DE LUXO ================= -->
    <section class="page-a4 cover-page">
        <div class="cover-top-bar">
            <div class="cover-logo-capsule">
                <img src="{logo_data_uri}" alt="Spa do Colchão Hotelaria" class="cover-logo-img">
            </div>
            <div class="cover-process-tag">
                PROCESSO CORPORATIVO: <span>PROP-2026-FOZ-393</span><br>
                CLASSIFICAÇÃO: <span>ESTRITAMENTE CONFIDENCIAL / B2B</span>
            </div>
        </div>

        <div class="cover-center-block">
            <div class="cover-badge-category">
                <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M12 2L2 7l10 5 10-5-10-5z"></path><path d="M2 17l10 5 10-5"></path><path d="M2 12l10 5 10-5"></path></svg>
                Divisão de Engenharia & Contratos Corporativos
            </div>

            <h1 class="cover-main-h1">
                Plano Diretor de Revitalização Hoteleira
            </h1>

            <p class="cover-lead-p">
                Dossiê Técnico, Memorial de Engenharia Industrial & Proposta Comercial Corporativa para Reconstrução Estrutural de <strong>393 Camas Hoteleiras (Colchão Solteirão 0,93 × 2,03 m + Sommier Box)</strong> e <strong>78 Pillow Tops King (2,00 × 2,00 m)</strong>.
            </p>

            <div class="cover-recipient-card">
                <span class="cover-recipient-label">Proposta Elaborada Exclusivamente Para:</span>
                <div class="cover-recipient-name">HOTEL FOZ DO IGUAÇU</div>
                <div class="cover-recipient-sub">
                    À Diretoria Geral, Gerência Operacional, Comitê de Compras & Governança<br>
                    Av. Brasil, Centro — Foz do Iguaçu / PR
                </div>
            </div>
        </div>

        <div class="cover-bottom-bar">
            <div class="cover-footer-meta">
                Proponente: <strong>Spa do Colchão Hotelaria</strong> • Consultoria: <strong>Douglas</strong> (+55 45 99937-1901)<br>
                Emissão Oficial: <strong>29 de Setembro de 2026</strong> • Validade: <strong>30 dias</strong> • Foz do Iguaçu / PR
            </div>
            <div class="cover-badges-right">
                <span class="cover-badge-pill">12 Meses Garantia</span>
                <span class="cover-badge-pill">SLA em Ondas</span>
                <span class="cover-badge-pill" style="border-color: #38bdf8; color: #38bdf8;">-65,8% CapEx</span>
            </div>
        </div>
    </section>

    <!-- ================= PÁGINA 2: FICHA CADASTRAL & INDICADORES ================= -->
    <section class="page-a4">
        <header class="doc-header">
            <div class="doc-header-brand">
                <img src="{logo_data_uri}" alt="Spa do Colchão" class="doc-logo">
                <span class="doc-division-badge">Ficha do Projeto</span>
            </div>
            <div class="doc-header-meta">
                Processo: <strong>PROP-2026-FOZ-393</strong><br>
                Data: <strong>29/09/2026</strong>
            </div>
        </header>

        <div class="page-body">
            <div class="section-eyebrow">Identificação das Partes</div>
            <h2 class="section-title">Ficha Cadastral do Projeto & Métricas Principais</h2>
            <p class="section-lead">
                Informações consolidadas de registro cadastral, especificação volumétrica do contrato e principais indicadores econômicos calculados para o empreendimento.
            </p>

            <div class="cadastral-card">
                <div class="cadastral-grid">
                    <div class="cadastral-item">
                        <span class="cadastral-label">Estabelecimento Contratante</span>
                        <span class="cadastral-val">Hotel Foz do Iguaçu</span>
                        <span style="font-size: 10.5px; color: var(--slate-muted);">Av. Brasil, Centro — Foz do Iguaçu / PR</span>
                    </div>
                    <div class="cadastral-item">
                        <span class="cadastral-label">Indústria Proponente / Executora</span>
                        <span class="cadastral-val">Spa do Colchão Hotelaria</span>
                        <span style="font-size: 10.5px; color: var(--slate-muted);">Parque Industrial — Foz do Iguaçu / PR</span>
                    </div>
                    <div class="cadastral-item">
                        <span class="cadastral-label">Escopo Total de Leitos</span>
                        <span class="cadastral-val" style="color: var(--teal-brand);">393 Camas Completas (Colchões + Boxes)</span>
                        <span style="font-size: 10.5px; color: var(--slate-muted);">+ 78 Pillow Tops King Casal (2,00 × 2,00 m — 3 cm)</span>
                    </div>
                    <div class="cadastral-item">
                        <span class="cadastral-label">Consultor Técnico Responsável</span>
                        <span class="cadastral-val">Douglas</span>
                        <span style="font-size: 10.5px; color: var(--teal-brand); font-weight: 700;">WhatsApp / Celular: +55 45 99937-1901</span>
                    </div>
                </div>
            </div>

            <div class="section-eyebrow">Destaques Estratégicos</div>
            <h3 style="font-size: 13.5px; font-weight: 800; color: var(--navy-dark); margin-bottom: 10px;">Indicadores de Viabilidade Hoteleira</h3>

            <div class="metrics-grid-3">
                <div class="metric-card">
                    <div class="metric-val" style="color: #166534;">65,8%</div>
                    <div class="metric-title">Economia de CapEx</div>
                    <div class="metric-desc">Preservação de mais de <strong>R$ 894.000,00</strong> no fluxo de caixa se comparado à compra de leitos novos.</div>
                </div>
                <div class="metric-card">
                    <div class="metric-val" style="color: var(--teal-brand);">393 Leitos</div>
                    <div class="metric-title">Operação em Ondas</div>
                    <div class="metric-desc">Coleta e entrega semanal fracionada de 20 a 30 quartos, com zero prejuízo de diárias ou inventário.</div>
                </div>
                <div class="metric-card gold">
                    <div class="metric-val" style="color: var(--gold-accent);">12 Meses</div>
                    <div class="metric-title">Garantia Industrial</div>
                    <div class="metric-desc">Garantia estrutural total com equipe de assistência técnica residente em Foz do Iguaçu.</div>
                </div>
            </div>

            <div style="background: var(--bg-card); border-left: 3px solid var(--teal-brand); padding: 12px 16px; border-radius: 4px; font-size: 11px; color: var(--slate-secondary); line-height: 1.5;">
                <strong>Certificação de Conformidade:</strong> O Spa do Colchão opera com espumas seladas e certificadas pelo INMETRO, tecidos tratados com barreiras antimicrobianas ativas e estrutura de reflorestamento com secagem em estufa.
            </div>
        </div>

        <footer class="doc-footer">
            <span class="doc-footer-company">Hotel Foz do Iguaçu • Ficha Cadastral do Projeto</span>
            <span class="doc-footer-page">Página 2 de 8</span>
        </footer>
    </section>

    <!-- ================= PÁGINA 3: CARTA FORMAL & PILARES ================= -->
    <section class="page-a4">
        <header class="doc-header">
            <div class="doc-header-brand">
                <img src="{logo_data_uri}" alt="Spa do Colchão" class="doc-logo">
                <span class="doc-division-badge">Sumário Executivo</span>
            </div>
            <div class="doc-header-meta">
                Processo: <strong>PROP-2026-FOZ-393</strong><br>
                Data: <strong>29/09/2026</strong>
            </div>
        </header>

        <div class="page-body">
            <div class="section-eyebrow">Apresentação Oficial</div>
            <h2 class="section-title">Carta Formal à Diretoria do Hotel Foz do Iguaçu</h2>
            
            <div class="letter-recipient">
                <strong>À Diretoria Geral, Gerência Operacional e Comitê de Compras</strong><br>
                Hotel Foz do Iguaçu — Foz do Iguaçu / PR<br>
                <em>A/C: Governança Geral, Compras e Controladoria</em>
            </div>

            <p class="letter-text">
                Prezados Senhores Diretores e Gestores,
            </p>

            <p class="letter-text">
                É com grande honra que o <strong>Spa do Colchão Hotelaria</strong> apresenta este Plano Diretor de Revitalização Hoteleira para os 393 leitos do <strong>Hotel Foz do Iguaçu</strong>. Como referência de hospitalidade na região das Cataratas, sabemos que o colchão é o ativo de maior impacto direto na nota de avaliação e na retenção dos hóspedes nas principais OTAs (Booking, Expedia e TripAdvisor).
            </p>

            <p class="letter-text">
                A aquisição de colchões novos no mercado hoteleiro impõe um desembolso vultoso de capital e custos logísticos elevados. Nossa solução de reengenharia industrial desmonta os leitos em fábrica, revisa e alinha termicamente as molas, substitui integralmente os blocos de espuma por espumas novas de alta densidade (D-33 / D-45) e reveste cada conjunto com novo tecido Jacquard matelassado de padrão superior, munido de barreiras ativas antiácaro, antimofo e retardante a chamas.
            </p>

            <p class="letter-text">
                O leito é devolvido com <strong>conforto, resiliência e estética de produto 100% novo</strong>, viabilizando uma redução orçamentária superior a <strong>65%</strong> em relação à compra de novos conjuntos no mercado.
            </p>

            <div style="margin-top: 14px;">
                <div class="section-eyebrow">Diretrizes do Fornecimento</div>
                <h3 style="font-size: 13.5px; font-weight: 800; color: var(--navy-dark); margin-bottom: 10px;">Pilares Fundamentais da Parceria</h3>

                <div class="pillars-grid-4">
                    <div class="pillar-card">
                        <div class="pillar-header">
                            <span class="pillar-badge">1</span>
                            <span class="pillar-title">Padrão Fabril Superior</span>
                        </div>
                        <p class="pillar-desc">Espumas técnicas D-33/D-45 de alto suporte de peso e tecidos jacquard hoteleiros de alta gramatura.</p>
                    </div>
                    <div class="pillar-card">
                        <div class="pillar-header">
                            <span class="pillar-badge">2</span>
                            <span class="pillar-title">Operação Sem Interrupção</span>
                        </div>
                        <p class="pillar-desc">Coleta e entrega semanal fracionada sem que nenhum quarto fique interditado no fim de semana.</p>
                    </div>
                    <div class="pillar-card">
                        <div class="pillar-header">
                            <span class="pillar-badge">3</span>
                            <span class="pillar-title">Economia Comprovada</span>
                        </div>
                        <p class="pillar-desc">Desconto oficial de escala gerando economia de R$ 83.832,00 sobre a tabela avulsa de reforma.</p>
                    </div>
                    <div class="pillar-card">
                        <div class="pillar-header">
                            <span class="pillar-badge">4</span>
                            <span class="pillar-title">Garantia & Assistência Local</span>
                        </div>
                        <p class="pillar-desc">Garantia estrutural de 12 meses com pronto atendimento presencial em Foz do Iguaçu.</p>
                    </div>
                </div>
            </div>
        </div>

        <footer class="doc-footer">
            <span class="doc-footer-company">Hotel Foz do Iguaçu • Sumário Executivo & Carta de Apresentação</span>
            <span class="doc-footer-page">Página 3 de 8</span>
        </footer>
    </section>

    <!-- ================= PÁGINA 4: MEMORIAL DESCRITIVO ================= -->
    <section class="page-a4">
        <header class="doc-header">
            <div class="doc-header-brand">
                <img src="{logo_data_uri}" alt="Spa do Colchão" class="doc-logo">
                <span class="doc-division-badge">Engenharia de Produto</span>
            </div>
            <div class="doc-header-meta">
                Norma: <strong>Padrão Hoteleiro Superior</strong><br>
                Auditoria: <strong>Controle de Qualidade Fabril</strong>
            </div>
        </header>

        <div class="page-body">
            <div class="section-eyebrow">Especificações Técnicas</div>
            <h2 class="section-title">Memorial Descritivo da Reengenharia dos Leitos</h2>
            <p class="section-lead">
                Cada leito passa por processo fabril de reengenharia mecânica e têxtil, recuperando a sustentação ortopédica ideal e a integridade higiênica exigida na hotelaria.
            </p>

            <div class="specs-grid">
                <!-- ITEM 1 -->
                <div class="spec-box">
                    <div class="spec-index">01</div>
                    <div class="spec-content">
                        <h4>Reforma Completa Colchão Solteirão (0,93 × 2,03 m) — 1 Lado (Uniface)</h4>
                        <p>
                            Substituição integral do revestimento externo por novo tecido Jacquard matelassado com fibra siliconada. Remoção de espumas fatigadas e aplicação de novo bloco selado de espuma de conforto D-33/D-45. Alinhamento térmico das molas, reforço perimetral de borda e isolante de base em polipropileno agulhado de alta gramatura.
                        </p>
                    </div>
                    <div class="spec-meta">
                        <div class="spec-meta-dim">0,93 × 2,03 m</div>
                        <div class="spec-meta-tag">100% Renovado</div>
                    </div>
                </div>

                <!-- ITEM 2 -->
                <div class="spec-box recommended">
                    <div class="spec-index" style="background: var(--teal-brand);">02</div>
                    <div class="spec-content">
                        <h4>Reforma Completa Colchão Solteirão (0,93 × 2,03 m) — DUPLA FACE (Two Sides)</h4>
                        <p>
                            Construção simétrica nas duas faces (superior e inferior). Ambas recebem novo tecido jacquard matelassado e camadas idênticas de espuma técnica selada D-33/D-45. Permite o rodízio quinzenal de giro e virada (360°), evitando vícios de postura, uniformizando o desgaste e <strong>duplicando a vida útil operacional</strong> do colchão no hotel.
                        </p>
                    </div>
                    <div class="spec-meta">
                        <div class="spec-meta-dim">0,93 × 2,03 m</div>
                        <div class="spec-meta-tag" style="color: #0f766e; font-weight: 800;">Padrão Recomendado</div>
                    </div>
                </div>

                <!-- ITEM 3 -->
                <div class="spec-box">
                    <div class="spec-index">03</div>
                    <div class="spec-content">
                        <h4>Reforma Completa Sommier / BOX Solteirão (0,93 × 2,03 m)</h4>
                        <p>
                            Desmontagem e inspeção da armação de madeira maciça. Travamento dos pontos de ancoragem para eliminação definitiva de rangidos e oscilações. Instalação de novo estrado e feltro amortecedor de impacto. Troca total da forração lateral e superior por tecido de alta resistência combinando com os colchões, cantoneiras e revisão dos pés niveladores.
                        </p>
                    </div>
                    <div class="spec-meta">
                        <div class="spec-meta-dim">0,93 × 2,03 m</div>
                        <div class="spec-meta-tag">Estrutura Estável</div>
                    </div>
                </div>

                <!-- ITEM 4 -->
                <div class="spec-box">
                    <div class="spec-index">04</div>
                    <div class="spec-content">
                        <h4>Pillow Top King com Elástico Reforçado (2,00 × 2,00 m — 3 cm de Espessura)</h4>
                        <p>
                            Sobrecolchão de acolhimento hoteleiro superior. Desenvolvido para permitir a conversão instantânea de duas camas solteirão (0,93+0,93m) em uma espaçosa cama King de casal, preenchendo qualquer fresta central com conforto contínuo e macio. Tecido maquinetado de toque sedoso e 4 elásticos largos de alta tensão nas quatro extremidades.
                        </p>
                    </div>
                    <div class="spec-meta">
                        <div class="spec-meta-dim">2,00 × 2,00 m</div>
                        <div class="spec-meta-tag" style="color: var(--gold-accent);">Conforto King</div>
                    </div>
                </div>
            </div>

            <div style="background: var(--bg-card); border-left: 3px solid var(--teal-brand); padding: 10px 14px; border-radius: 4px; font-size: 10.5px; color: var(--slate-secondary); margin-top: 14px;">
                <strong>Tratamentos Tecnológicos Ativos:</strong> Todos os materiais têxteis e espumas utilizados possuem laudo de atoxidade, proteção antimicrobiana (íons de prata contra ácaros e fungos) e certificação de retardância à propagação de chamas conforme normas da ABNT.
            </div>
        </div>

        <footer class="doc-footer">
            <span class="doc-footer-company">Hotel Foz do Iguaçu • Memorial Descritivo de Engenharia</span>
            <span class="doc-footer-page">Página 4 de 8</span>
        </footer>
    </section>

    <!-- ================= PÁGINA 5: MATRIZ DE PREÇOS & ESTUDO CAPEX ================= -->
    <section class="page-a4">
        <header class="doc-header">
            <div class="doc-header-brand">
                <img src="{logo_data_uri}" alt="Spa do Colchão" class="doc-logo">
                <span class="doc-division-badge">Análise Financeira</span>
            </div>
            <div class="doc-header-meta">
                Tabela Oficial: <strong>Unitário vs. Lotes Acima de 20 un.</strong><br>
                Moeda: <strong>BRL (R$)</strong>
            </div>
        </header>

        <div class="page-body">
            <div class="section-eyebrow">Matriz Comercial</div>
            <h2 class="section-title">Tabela de Preços Unitários & Condições por Escala</h2>
            <p class="section-lead">
                A política de precificação prevê faixas de incentivo progressivo para lotes superiores a 20 unidades, permitindo que o hotel planeje o investimento por etapas ou por blocos de apartamentos.
            </p>

            <table class="table-corporate">
                <thead>
                    <tr>
                        <th style="width: 42%;">Descrição do Item / Serviço</th>
                        <th style="width: 14%;">Medida</th>
                        <th style="width: 15%;">Unitário Normal</th>
                        <th style="width: 15%;">Lote > 20 un.</th>
                        <th style="width: 14%;">Economia / un.</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>
                            <strong>Reforma Completa Colchão Solteirão (1 Lado)</strong><br>
                            <small style="color: var(--slate-muted);">Tecido novo + novas espumas + revisão interna de molas</small>
                        </td>
                        <td>0,93 × 2,03 m</td>
                        <td class="price-bold">R$ 795,00</td>
                        <td class="price-highlight">R$ 695,00</td>
                        <td><span class="savings-tag">- R$ 100,00 (-12,6%)</span></td>
                    </tr>
                    <tr>
                        <td>
                            <strong>Reforma Completa Colchão Solteirão (DUPLA FACE)</strong><br>
                            <small style="color: var(--slate-muted);">2 lados novos + novas espumas em ambas as faces + reparos</small>
                        </td>
                        <td>0,93 × 2,03 m</td>
                        <td class="price-bold">R$ 975,00</td>
                        <td class="price-highlight">R$ 799,00</td>
                        <td><span class="savings-tag">- R$ 176,00 (-18,1%)</span></td>
                    </tr>
                    <tr>
                        <td>
                            <strong>Reforma Completa Sommier / BOX Solteirão</strong><br>
                            <small style="color: var(--slate-muted);">Travamento estrutural + tecido lateral e tampo novos</small>
                        </td>
                        <td>0,93 × 2,03 m</td>
                        <td class="price-bold">R$ 375,00</td>
                        <td class="price-highlight">R$ 290,00</td>
                        <td><span class="savings-tag">- R$ 85,00 (-22,7%)</span></td>
                    </tr>
                    <tr>
                        <td>
                            <strong>Pillow Top King com Elástico (3 cm de altura)</strong><br>
                            <small style="color: var(--slate-muted);">Espuma selada + tecido acolchoado para unificação de leitos</small>
                        </td>
                        <td>2,00 × 2,00 m</td>
                        <td class="price-bold">R$ 1.185,00</td>
                        <td class="price-highlight">R$ 997,00</td>
                        <td><span class="savings-tag">- R$ 188,00 (-15,9%)</span></td>
                    </tr>
                </tbody>
            </table>

            <div style="margin-top: 10px;">
                <div class="section-eyebrow">Estudo Comparativo de Viabilidade</div>
                <h3 style="font-size: 13.5px; font-weight: 800; color: var(--navy-dark); margin-bottom: 8px;">Análise Financeira: Aquisição de Colchões Novos vs. Reforma Estrutural</h3>

                <table class="table-corporate" style="margin-bottom: 10px;">
                    <thead>
                        <tr>
                            <th>Cenário de Investimento (393 Camas Dupla Face + Box)</th>
                            <th>Custo Médio / Leito</th>
                            <th>Investimento Total</th>
                            <th>Impacto no Fluxo de Caixa</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td>
                                <strong>Cenário A: Compra de Colchões e Boxes Novos no Mercado</strong><br>
                                <small style="color: var(--slate-muted);">Aquisição de conjuntos solteirão equivalentes com frete interestadual</small>
                            </td>
                            <td>R$ 3.450,00</td>
                            <td style="color: #dc2626; font-weight: 800; font-variant-numeric: tabular-nums;">R$ 1.355.850,00</td>
                            <td style="font-size: 10px; color: #dc2626; font-weight: 700;">Alto impacto de CapEx</td>
                        </tr>
                        <tr style="background: var(--teal-subtle);">
                            <td>
                                <strong>Cenário B: Reforma Estrutural Spa do Colchão (Combo DF)</strong><br>
                                <small style="color: var(--teal-brand); font-weight: 700;">Reconstrução total padrão novo com garantia de 12 meses</small>
                            </td>
                            <td class="price-highlight">R$ 1.174,00</td>
                            <td class="price-highlight" style="font-size: 13px;">R$ 461.382,00</td>
                            <td style="font-size: 10px; color: #166534; font-weight: 800;">Economia Direta de R$ 894.468,00</td>
                        </tr>
                    </tbody>
                </table>

                <div style="background: #f0fdf4; border: 1px solid #bbf7d0; border-radius: 6px; padding: 12px 16px; display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <span style="font-size: 11.5px; font-weight: 800; color: #166534;">ECONOMIA PATRIMONIAL LÍQUIDA:</span>
                        <span style="font-size: 11px; color: #14532d; display: block; margin-top: 2px;">O Hotel Foz do Iguaçu preserva <strong>R$ 894.468,00</strong> no caixa, obtendo leitos idênticos a novos com garantia de fábrica.</span>
                    </div>
                    <div style="font-size: 20px; font-weight: 900; color: #166534; font-variant-numeric: tabular-nums;">
                        - 65,9%
                    </div>
                </div>
            </div>
        </div>

        <footer class="doc-footer">
            <span class="doc-footer-company">Hotel Foz do Iguaçu • Matriz de Preços & Estudo de CapEx</span>
            <span class="doc-footer-page">Página 5 de 8</span>
        </footer>
    </section>

    <!-- ================= PÁGINA 6: COMBOS DE FECHAMENTO TOTAL ================= -->
    <section class="page-a4">
        <header class="doc-header">
            <div class="doc-header-brand">
                <img src="{logo_data_uri}" alt="Spa do Colchão" class="doc-logo">
                <span class="doc-division-badge" style="background: var(--gold-subtle); color: var(--gold-accent); border-color: var(--gold-border);">Pacotes Turnkey</span>
            </div>
            <div class="doc-header-meta">
                Escopo: <strong>Fechamento Integral das 393 Camas</strong><br>
                Desconto Máximo de Escala
            </div>
        </header>

        <div class="page-body">
            <div class="section-eyebrow">Soluções Corporativas Globais</div>
            <h2 class="section-title">Grandes Combos de Fechamento Total do Hotel</h2>
            <p class="section-lead">
                Para o fechamento integral dos 393 conjuntos de leitos do Hotel Foz do Iguaçu, estruturamos pacotes com condições comerciais extraordinárias, assegurando a maior taxa de desconto possível.
            </p>

            <div class="combos-container">
                <!-- COMBO 1 -->
                <div class="combo-row">
                    <div class="combo-info">
                        <span style="font-size: 9.5px; font-weight: 800; text-transform: uppercase; color: var(--slate-muted); background: var(--border-light); padding: 2px 7px; border-radius: 4px;">Opção A</span>
                        <h4 style="margin-top: 4px;">Combo 393 Camas Solteirão (1 Lado + Box)</h4>
                        <p>
                            Renovação completa de 393 colchões solteirão uniface (0,93 × 2,03 m) + 393 sommiers box correspondentes. Ideal para revitalização econômica de grande impacto visual e de conforto.
                        </p>
                    </div>
                    <div class="combo-values">
                        <div class="combo-de">Valor Normal: R$ 459.810,00</div>
                        <div class="combo-por">R$ 387.105,00</div>
                        <div class="combo-eco">Economia de R$ 72.705,00</div>
                        <div style="font-size: 9.5px; color: var(--slate-muted); margin-top: 2px;">R$ 985,00 por conjunto completo</div>
                    </div>
                </div>

                <!-- COMBO 2 (FEATURED) -->
                <div class="combo-row highlighted">
                    <div class="combo-info">
                        <span style="font-size: 9.5px; font-weight: 800; text-transform: uppercase; color: #ffffff; background: var(--teal-brand); padding: 2px 7px; border-radius: 4px;">Opção B • Mais Recomendada</span>
                        <h4 style="margin-top: 4px; color: var(--teal-brand);">Combo 393 Camas Solteirão (DUPLA FACE + Box)</h4>
                        <p>
                            393 colchões solteirão dupla face (Two Sides) de alta resistência com rodízio pleno + 393 sommiers box completos. Máxima longevidade estrutural e garantia de durabilidade para a operação hoteleira.
                        </p>
                    </div>
                    <div class="combo-values" style="border-color: var(--teal-border); background: #ffffff;">
                        <div class="combo-de">Valor Normal: R$ 530.550,00</div>
                        <div class="combo-por">R$ 461.382,00</div>
                        <div class="combo-eco">Economia de R$ 69.168,00</div>
                        <div style="font-size: 9.5px; color: var(--teal-brand); font-weight: 700; margin-top: 2px;">R$ 1.174,00 por conjunto completo</div>
                    </div>
                </div>

                <!-- COMBO 3 -->
                <div class="combo-row">
                    <div class="combo-info">
                        <span style="font-size: 9.5px; font-weight: 800; text-transform: uppercase; color: var(--slate-muted); background: var(--border-light); padding: 2px 7px; border-radius: 4px;">Opção C • Upgrade Suítes</span>
                        <h4 style="margin-top: 4px;">Combo 78 Pillow Tops King Casal (2,00 × 2,00 m — 3 cm)</h4>
                        <p>
                            Lote de 78 pillow tops com elásticos para versatilidade dos quartos do hotel, unificando dois leitos solteirão em camas King de casal com padrão superior de acolhimento e acabamento.
                        </p>
                    </div>
                    <div class="combo-values">
                        <div class="combo-de">Valor Normal: R$ 92.430,00</div>
                        <div class="combo-por">R$ 77.766,00</div>
                        <div class="combo-eco">Economia de R$ 14.664,00</div>
                        <div style="font-size: 9.5px; color: var(--slate-muted); margin-top: 2px;">R$ 997,00 por unidade King</div>
                    </div>
                </div>
            </div>

            <!-- MASTER TURNKEY BANNER -->
            <div class="master-banner">
                <div>
                    <div class="master-banner-title">Pacote Master Turnkey Total (Opção B + Opção C)</div>
                    <div class="master-banner-sub">393 Camas Dupla Face + 393 Boxes + 78 Pillow Tops King (Total de 864 peças)</div>
                    <div style="font-size: 10px; color: #cbd5e1; margin-top: 4px;">De <s>R$ 622.980,00</s> por apenas:</div>
                </div>
                <div style="text-align: right;">
                    <div class="master-banner-price">R$ 539.148,00</div>
                    <div style="background: #22c55e; color: #052e16; font-size: 10px; font-weight: 800; padding: 3px 9px; border-radius: 12px; display: inline-block; margin-top: 2px;">
                        Economia Consolidada: R$ 83.832,00
                    </div>
                </div>
            </div>

            <div style="font-size: 11px; color: var(--slate-secondary); margin-top: 12px; line-height: 1.5;">
                <strong>Condições de Faturamento Corporativo:</strong> Pagamento direto de fábrica com parcelamento vinculado às medições parciais de entrega de cada lote. Faturamento via Boleto Bancário com emissão de Nota Fiscal Eletrônica.
            </div>
        </div>

        <footer class="doc-footer">
            <span class="doc-footer-company">Hotel Foz do Iguaçu • Combos Oficiais de Fechamento Total</span>
            <span class="doc-footer-page">Página 6 de 8</span>
        </footer>
    </section>

    <!-- ================= PÁGINA 7: LOGÍSTICA & SLA HOTELEIRO ================= -->
    <section class="page-a4">
        <header class="doc-header">
            <div class="doc-header-brand">
                <img src="{logo_data_uri}" alt="Spa do Colchão" class="doc-logo">
                <span class="doc-division-badge">Logística & Operações</span>
            </div>
            <div class="doc-header-meta">
                Modelo: <strong>Logística em Ondas Hoteleiras</strong><br>
                SLA: <strong>Zero Interdição de Inventário</strong>
            </div>
        </header>

        <div class="page-body">
            <div class="section-eyebrow">Planejamento Operacional</div>
            <h2 class="section-title">Logística Fracionada & Cronograma de Execução</h2>
            <p class="section-lead">
                Sabemos que a operação de um hotel de 393 leitos não pode sofrer paralisações. Por isso, desenvolvemos um fluxo logístico em ondas perfeitamente alinhado com os dias de menor ocupação e os ciclos de check-out.
            </p>

            <div class="flow-grid-4">
                <div class="flow-step">
                    <div class="flow-step-num">ETAPA 01</div>
                    <div class="flow-step-title">Retirada Programada</div>
                    <div class="flow-step-desc">Coleta de lotes de 20 a 30 quartos na segunda-feira pela manhã, após o check-out dos hóspedes.</div>
                </div>
                <div class="flow-step">
                    <div class="flow-step-num">ETAPA 02</div>
                    <div class="flow-step-title">Higienização & Reparo</div>
                    <div class="flow-step-desc">Tratamento antiácaro, revisão de molas e travamento das armações dos boxes na fábrica.</div>
                </div>
                <div class="flow-step">
                    <div class="flow-step-num">ETAPA 03</div>
                    <div class="flow-step-title">Reespumação & Tecidos</div>
                    <div class="flow-step-desc">Aplicação de espumas D-33/D-45 novas e revestimento com novo jacquard matelassado.</div>
                </div>
                <div class="flow-step">
                    <div class="flow-step-num">ETAPA 04</div>
                    <div class="flow-step-title">Devolução Embalada</div>
                    <div class="flow-step-desc">Retorno dos leitos em embalagem plástica lacrada até sexta-feira para o check-in do fim de semana.</div>
                </div>
            </div>

            <div class="sla-box">
                <h4>Diretrizes do Acordo de Nível de Serviço (SLA Hoteleiro):</h4>
                <ul>
                    <li><strong>Transporte Próprio e Equipe Treinada:</strong> Coleta e entrega realizadas em caminhão baú higienizado e equipe uniformizada, com o devido cuidado nos elevadores e corredores do hotel;</li>
                    <li><strong>Lotes Moduláveis:</strong> A quantidade por ciclo (ex: 20, 25 ou 30 camas) é adaptada semanalmente de acordo com a taxa de ocupação informada pela governança do hotel;</li>
                    <li><strong>Embalagem Plástica Selada de Fábrica:</strong> Todos os colchões e boxes são entregues rigorosamente limpos e envelopados, prontos para uso imediato;</li>
                    <li><strong>Descarte Sustentável de Resíduos (ESG):</strong> Todo o tecido e espuma antiga removida é encaminhada para descarte ecológico ou reciclagem industrial autorizada, com emissão de declaração de destinação ambiental.</li>
                </ul>
            </div>

            <div style="background: var(--teal-subtle); border: 1.5px solid var(--teal-border); border-radius: 6px; padding: 14px 18px; margin-top: 8px;">
                <div style="display: flex; justify-content: space-between; align-items: center;">
                    <div>
                        <strong style="font-size: 12px; color: var(--navy-dark); display: block;">Amostra Piloto Sem Custo de Homologação:</strong>
                        <span style="font-size: 11px; color: var(--slate-secondary);">
                            Disponibilizamos a execução imediata de <strong>1 a 2 conjuntos completos (colchão + box)</strong> em um quarto piloto para validação técnica prévia da governança e da diretoria do Hotel Foz do Iguaçu.
                        </span>
                    </div>
                    <div style="font-size: 11px; font-weight: 800; color: var(--teal-brand); background: #ffffff; padding: 5px 12px; border-radius: 20px; white-space: nowrap; margin-left: 16px;">
                        Piloto Disponível
                    </div>
                </div>
            </div>
        </div>

        <footer class="doc-footer">
            <span class="doc-footer-company">Hotel Foz do Iguaçu • Acordo de Nível de Serviço Logístico</span>
            <span class="doc-footer-page">Página 7 de 8</span>
        </footer>
    </section>

    <!-- ================= PÁGINA 8: TERMO DE ACEITE & ASSINATURAS ================= -->
    <section class="page-a4">
        <header class="doc-header">
            <div class="doc-header-brand">
                <img src="{logo_data_uri}" alt="Spa do Colchão" class="doc-logo">
                <span class="doc-division-badge">Termo Contratual</span>
            </div>
            <div class="doc-header-meta">
                Status: <strong>Pronto para Formalização</strong><br>
                Garantia: <strong>12 Meses Estrutural</strong>
            </div>
        </header>

        <div class="page-body">
            <div class="section-eyebrow">Instrumento Jurídico & Comercial</div>
            <h2 class="section-title">Termo de Homologação, Aceite & Assinaturas</h2>
            <p class="section-lead">
                A aprovação deste termo consolida as condições comerciais especiais ofertadas nesta proposta, autorizando a emissão do contrato formal de fornecimento e o agendamento do cronograma industrial.
            </p>

            <div class="formal-clauses">
                <strong>Condições Gerais e Cláusulas Contratuais:</strong>
                <ol>
                    <li><strong>Validade da Proposta:</strong> As condições e valores deste dossiê são válidos por 30 (trinta) dias a contar da data de sua emissão oficial.</li>
                    <li><strong>Garantia Fabril:</strong> O Spa do Colchão assegura garantia integral de 12 (doze) meses contra deformações estruturais de espumas, quebra de molas ou falhas na estrutura de madeira dos boxes.</li>
                    <li><strong>Medições e Pagamentos:</strong> O faturamento será processado progressivamente mediante a entrega e conferência de cada lote pela governança do hotel, conforme cronograma acordado.</li>
                    <li><strong>Foro:</strong> Fica eleito o foro da Comarca de Foz do Iguaçu — PR para dirimir quaisquer dúvidas decorrentes do presente fornecimento.</li>
                </ol>
            </div>

            <div class="acceptance-box">
                <strong style="font-size: 11.5px; color: var(--navy-dark); text-transform: uppercase; letter-spacing: 0.5px; display: block; margin-bottom: 8px;">
                    Dados de Homologação pelo Hotel Foz do Iguaçu:
                </strong>

                <div class="acceptance-grid">
                    <div class="acc-field">
                        <strong>Razão Social / Nome Fantasia:</strong>
                        Hotel Foz do Iguaçu Ltda.
                    </div>
                    <div class="acc-field">
                        <strong>CNPJ / Inscrição Estadual:</strong>
                        ________________________________________
                    </div>
                    <div class="acc-field">
                        <strong>Representante Autorizado / Cargo:</strong>
                        ________________________________________
                    </div>
                    <div class="acc-field">
                        <strong>Telefone / WhatsApp de Contato:</strong>
                        ________________________________________
                    </div>
                    <div class="acc-field" style="grid-column: span 2;">
                        <strong>Opção Comercial Aprovada:</strong>
                        [&nbsp;&nbsp;] Combo 393 Camas Dupla Face + Box (R$ 461.382)&nbsp;&nbsp;&nbsp;&nbsp;
                        [&nbsp;&nbsp;] Combo Master com 78 Pillows (R$ 539.148)<br>
                        [&nbsp;&nbsp;] Combo 393 Camas 1 Lado + Box (R$ 387.105)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
                        [&nbsp;&nbsp;] Outra Quantidade / Lote Parcial
                    </div>
                    <div class="acc-field" style="grid-column: span 2;">
                        <strong>Data Pretendida para Início do Lote Piloto:</strong>
                        _____ / _____ / 2026
                    </div>
                </div>
            </div>

            <!-- QUADRO FORMAL DE ASSINATURAS -->
            <div class="signatures-grid">
                <div class="sig-block">
                    <div class="sig-line"></div>
                    <div class="sig-name">HOTEL FOZ DO IGUAÇU</div>
                    <div class="sig-role">Diretoria Geral / Gerência Operacional</div>
                    <div class="sig-company">De Acordo em _____ / _____ / 2026</div>
                </div>

                <div class="sig-block">
                    <div class="sig-line"></div>
                    <div class="sig-name">DOUGLAS</div>
                    <div class="sig-role">Consultoria Comercial & Projetos Corporativos</div>
                    <div class="sig-company">Spa do Colchão Hotelaria — (45) 99937-1901</div>
                </div>
            </div>
        </div>

        <footer class="doc-footer">
            <span class="doc-footer-company">Spa do Colchão Hotelaria • Parque Industrial — Foz do Iguaçu/PR</span>
            <span class="doc-footer-page">Página 8 de 8</span>
        </footer>
    </section>

</body>
</html>
"""

output_html = '/Volumes/Work/backup/HOTEL-FOZ-DO-IGUACU/dossie_corporativo.html'
with open(output_html, 'w', encoding='utf-8') as f:
    f.write(html_content)

print("dossie_corporativo.html updated to 8 pages with full luxury cover and improved spacing!")
